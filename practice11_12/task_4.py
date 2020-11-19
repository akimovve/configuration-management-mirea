from hypothesis import given
from hypothesis.strategies import builds, integers, recursive

# Задание 4. Генерирация случайных бинарных деревьев
class Node:

	# Инициализация узла
	# @param val - число (значение)
	# @param nxt - потомок (по умолчанию None)
	def __init__(self, val, nxt=None):
		self.__val = val
		self.__left = None
		self.__right = None
		if nxt is None:
			return
		if self.__val < nxt.__val:
			self.__right = nxt
		else:
			self.__left = nxt

	# Добавление узла (в зависимости от значения)
	# @return - узел
	def add(self, val):
		if self.__val is None or self.__val == val:
			self.__val = val
			return self
		if self.__val < val:
			if self.__right is None:
				self.__right = Node(val)
			else:
				self.__right.add(val)
		else:
			if self.__left is None:
				self.__left = Node(val)
			else:
				self.__left.add(val)
		return self

	# Поиск по значению
	def find_by_val(self, val):
		if self.__val is None:
			return False
		if self.__val == val:
			return True
		if self.__val < val:
			return self.__right.find_by_val(val)
		return self.__left.find_by_val(val)

	def count_branches_height(self):
		right_height = left_height = 0
		if self.__right is not None:
			right_height = self.__right.height()
		if self.__left is not None:
			left_height = self.__left.height()
		return left_height, right_height

	# Подсчёт высоты дерева
	def height(self):
		if self.__val is None:
			return 0
		return max(self.count_branches_height()) + 1

	# Вывод дерева
	def print(self, depth):
		if self.__right is not None:
			self.__right.print(depth + 1)
		print("\t" * depth, end="")
		print(self.__val, end=" <\n")
		if self.__left is not None:
			self.__left.print(depth + 1)


# Тестирование
@given(x=recursive(
		builds(Node, integers()),
		lambda i: builds(Node, integers(), i), max_leaves=100),
		a=integers(),
		b=integers()
)
def test_property(x, a, b):
	# Поиск по ключу
	x.add(a)
	x.add(b)
	assert x.find_by_val(a) and x.find_by_val(b)

	# Высота
	prev = x.height()
	assert 0 < prev < 102
	new = x.add(a).height()
	assert new == prev or new == prev + 1

	x.print(0)
	print("****************************************************************")
