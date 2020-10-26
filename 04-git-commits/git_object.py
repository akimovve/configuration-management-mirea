import os
import zlib
import binascii
from graphviz import Digraph
from type_commit import Type


### Класс-обработчик для получения содержания объектов в .git ###
class GitHandler:
	def __init__(self, path):
		self._path = path
		self._raw_data = None
		self._data = None
		self._type = None
		self._size = None
		self._contents = None
		with open(self._path, 'rb') as f:
			self._raw_data = f.read()
		self._data = zlib.decompress(self._raw_data)

	def get_data(self):
		return self._data

	# Возвращает тип объекта
	def type(self):
		if self._type is None:
			self._type = self._data.split(b' ', maxsplit=1)[0].decode()
		return self._type

	# Возвращает содержимое git-объекта
	def contents(self):
		return self._data.split(b'\x00', maxsplit=1)[1]

	# Возвращает размер объекта
	def size(self):
		if self._size is None:
			self._size = self._data.split(b'\x00', maxsplit=1)[0]
			self._size = self._size.split(b' ', maxsplit=1)[1]
			self._size = int(self._size)
		return self._size


### Классы для сохранения коммитов и деревьев ###
class Commit:
	def __init__(self, tree, parent, author, comment):
		self.tree = tree
		self.parent = parent
		self.author = author
		self.comment = comment


class Tree:
	def __init__(self, deps):
		self.deps = deps


### Класс, отвечающий за объекты в .git ###
class GitObject:
	def __init__(self, repo_path):
		self._objects_path = '/.git/objects'
		self._repo_path = repo_path
		self._objects = {}
		self.hash_files()

	def hash_files(self):
		for root, dirs, files in os.walk(self._repo_path + self._objects_path):
			for name in dirs:
				if name != 'info' or name != 'pack':
					for r, d, f in os.walk('{}{}/{}'.format(
							self._repo_path,
							self._objects_path,
							name)
					):
						for n in f:
							self.transform_objects(name + n)

	def transform_objects(self, hash_code):
		parent = None
		hash_code_tree = None
		author = None
		contents = []
		git_handler = GitHandler(
			'{}{}/{}/{}'.format(
				self._repo_path,
				self._objects_path,
				hash_code[0:2],
				hash_code[2:])
		)
		git_obj_type = git_handler.type()
		git_obj_contents = git_handler.contents()

		if git_obj_type == Type.COMMIT.value:
			contents = list(
				filter(
					None, git_obj_contents.decode().splitlines()
				)
			)
			for con in contents:
				if con.startswith(Type.PARENT.value):
					parent = con[7:]
				elif con.startswith(Type.TREE.value):
					hash_code_tree = con[5:]
				elif con.startswith(Type.AUTHOR.value):
					author = ' '.join(con.split()[1:4])
			self._objects[hash_code] = Commit(hash_code_tree, parent, author, contents[-1])
		elif git_obj_type == Type.TREE.value:
			while git_obj_contents != b'':
				file_mode, git_obj_contents = git_obj_contents.split(b' ', maxsplit=1)
				file_name, git_obj_contents = git_obj_contents.split(b'\x00', maxsplit=1)
				sha_1, git_obj_contents = git_obj_contents[:20], git_obj_contents[20:]
				sha_1 = binascii.hexlify(sha_1).decode()
				file_mode = file_mode.decode()
				file_name = file_name.decode()
				contents.append((file_mode, file_name, sha_1))
				self._objects[hash_code] = Tree(contents)
		else:
			pass

	@staticmethod
	def note_commit(f, s, t):
		return '[{}]\n{}\n"{}"'.format(f, t, s)

	def start(self):
		dot = Digraph(name='Commits Graph', comment='All local commits')
		for commit, object_commit in self._objects.items():
			if type(object_commit) is Commit:
				dot.node(commit, self.note_commit(Type.COMMIT.name, object_commit.comment, commit))
				dot.edge(commit, object_commit.tree)
				if object_commit.parent is not None:
					dot.edge(commit, object_commit.parent)
			elif type(object_commit) is Tree:
				dot.node(commit, '[{}]\n{}'.format(Type.TREE.name, commit))
				for dep in object_commit.deps:
					if dep[0] != '40000':
						dot.edge(commit, self.note_commit(Type.BLOB.name, dep[1], dep[2]))
					else:
						dot.edge(commit, dep[2])
		print(dot.source)

### Ресурс: https://gist.github.com/leonidessaguisagjr/594cd8fbbc9b18a1dde5084d981b8028 ###
