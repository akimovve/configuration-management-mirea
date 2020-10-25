from enum import Enum


class Type(Enum):
	TREE = 'tree'
	PARENT = 'parent'
	AUTHOR = 'author'
	COMMITTER = 'committer'

	@staticmethod
	def list():
		return list(map(lambda c: c.value, Type))
