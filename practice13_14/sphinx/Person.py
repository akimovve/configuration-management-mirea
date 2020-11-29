class Person:
	"""
	Модель (класс) человек.
	"""

	def __init__(self, name, family_name, age):
		"""
		Конструктор класса человек.

		:param name: Имя доктора.
		:type name: str
		:param family_name: Фамилия доктора.
		:type family_name: str
		:param age: Возраст доктора.
		:type age: int
		"""
		self.__name = name
		self.__family_name = family_name
		self.__age = age

	def __str__(self):
		"""
		Приведение объекта класса к строке.

		:return: Свойства класса.
		:rtype: str
		"""
		s = "\n\tName: {} {}\n\tAge: {}\n".format(str(self.__name), str(self.__family_name), str(self.__age))
		return s
