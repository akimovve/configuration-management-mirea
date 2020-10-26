from enum import Enum


### Перечисление из ключевых слов ###
class Type(Enum):
	TREE = 'tree'
	COMMIT = 'commit'
	BLOB = 'blob'
	PARENT = 'parent'
	AUTHOR = 'author'

	@staticmethod
	def list():
		return list(map(lambda c: c.value, Type))
