import os
from sys import argv
from git_object import GitObject

if __name__ == '__main__':
	repo_path = argv[1]
	os.chdir(repo_path)
	while not os.path.isdir('.git'):
		os.chdir('../')
		parent_path = os.getcwd()
		if parent_path == repo_path:
			raise OSError('fatal: not a git repository')
		repo_path = parent_path

	git = GitObject(repo_path).start()
