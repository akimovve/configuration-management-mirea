from sys import argv
import os
import parent_commit
from graphviz import Digraph

dot = Digraph(name='Commits Graph', comment='All local commits')

if __name__ == '__main__':
	current_path = argv[1]
	os.chdir(current_path)
	while not os.path.isdir('.git'):
		os.chdir('../')
		parent_path = os.getcwd()
		if parent_path == current_path:
			raise OSError('fatal: not a git repository')
		current_path = parent_path
	main_branch = open('.git/HEAD', 'r').read().split()[1]
	last_commit = open('.git/' + main_branch, 'r').read().replace('\n', '')
	parent_commit.Parent.get_parents(last_commit, dot)
	print(dot.source)
