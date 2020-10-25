import os
from type_commit import Type


class Tree:
	@staticmethod
	def get_trees(tree, dot):
		content_commit = list(
			filter(None,
				   os.popen('git cat-file -p ' + tree).read().replace('\t', ' ').split('\n'))
		)
		tree_dict = dict()
		for item in content_commit:
			name = item.split()[1]
			Tree.add(name, tree_dict, item)
		for key, value in tree_dict.items():
			for v in value:
				dot.edge('{} ({})'.format(tree, Type.TREE.name), '{} ({})'.format(v, key.upper()))
		if Type.TREE.value in tree_dict:
			for tr in tree_dict[Type.TREE.value]:
				Tree.get_trees(tr, dot)

	@staticmethod
	def add(name, tree_dict, item):
		if name not in tree_dict:
			if name == Type.TREE.value:
				tree_dict[name] = [item.split()[2]]
			else:
				tree_dict[name] = [' '.join(item.split()[2:len(item)])]
		else:
			if name == Type.TREE.value:
				tree_dict[name].append(item.split()[2])
			else:
				tree_dict[name].append(' '.join(item.split()[2:len(item)]))
