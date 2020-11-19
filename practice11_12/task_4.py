from hypothesis import given
from hypothesis.strategies import builds, integers, recursive

# Задание 4. Генерация случайных бинарных деревьев
class Node:

	# Инициализация узла
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	# Добавление узла (в зависимости от значения)
	# @return - узел
	def add(self, val):
		if self.val is None or self.val == val:
			self.val = val
			return self
		if self.val < val:
			if self.right is None:
				self.right = Node(val)
			else:
				self.right.add(val)
		else:
			if self.left is None:
				self.left = Node(val)
			else:
				self.left.add(val)
		return self

	# Поиск по значению
	def find_by_val(self, val):
		if self.val is None:
			return False
		if self.val == val:
			return True
		if self.val < val:
			return self.right.find_by_val(val)
		return self.left.find_by_val(val)

	def count_branches_height(self):
		right_height = left_height = 0
		if self.right is not None:
			right_height = self.right.height()
		if self.left is not None:
			left_height = self.left.height()
		return left_height, right_height

	# Подсчёт высоты дерева
	def height(self):
		if self.val is None:
			return 0
		return max(self.count_branches_height()) + 1

	def __repr__(self):
		return "Tree(val=%s, left=%s, right=%s)" % (self.val, self.left, self.right)


# Тестирование
@given(x=recursive(
		builds(Node, integers()),
		lambda i: builds(Node, integers(), i, i), max_leaves=100),
		a=integers(),
		b=integers()
)
def test_tree(x, a, b):
	# Поиск по ключу
	x.add(a)
	x.add(b)
	assert x.find_by_val(a) and x.find_by_val(b)

	# Высота
	prev = x.height()
	assert 0 < prev < 102
	new = x.add(a).height()
	assert new == prev or new == prev + 1

	print("\n\nВывод дерева:")
	print(x)
	print("****************************************************************")

test_tree()
