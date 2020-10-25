import os
from tree_commit import Tree
from type_commit import Type


class Parent:
	@staticmethod
	def get_parents(parent, dot):
		content_commit = list(
			filter(None,
				   os.popen('git cat-file -p ' + parent).read().split('\n'))
		)
		content_commit_dict = dict()
		to_fill = True
		for title in content_commit:
			if not to_fill:
				break
			name = title.split()[0]
			if name in Type.list():
				content_commit_dict[name] = ' '.join(title.split()[1:len(title)])
			elif to_fill:
				content_commit_dict['comment'] = title
				to_fill = False
		p = '{} ({}) (author {}) (comment {})'.format(parent, Type.PARENT.name,
													  content_commit_dict[Type.AUTHOR.value].split()[0],
													  content_commit_dict['comment'])
		dot.edge('commit', p)
		dot.edge(p, '{} ({})'.format(content_commit_dict[Type.TREE.value], Type.TREE.name))
		Tree.get_trees(content_commit_dict[Type.TREE.value], dot)
		if Type.PARENT.value in content_commit_dict:
			Parent.get_parents(content_commit_dict[Type.PARENT.value], dot)
