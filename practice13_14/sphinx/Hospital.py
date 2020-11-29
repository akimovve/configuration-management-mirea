class Hospital:
	"""
	Модель (класс) больница.
	"""

	def __init__(self, name, address):
		"""
		Конструктор класса больница.

		:param name: Название больницы.
		:type name: str
		:param address: Адрес больницы.
		:type address: str
		"""
		self.__name = name
		self.__address = address
		self.__doctors = []
		self.__nurses = []

	def add_doctor(self, doc):
		"""
		Добавление доктора в больницу.

		:param doc: Новый доктор.
		:type doc: Doctor
		:return: Доктор.
		:rtype: Doctor
		"""
		self.__doctors.append(doc)

	def add_nurse(self, nur):
		"""
		Добавление медсестры в больницу.

		:param nur: Новая медсестра.
		:type nur: Nurse
		:return: Медсестра.
		:rtype: Nurse
		"""
		self.__nurses.append(nur)

	def create_txt(self):
		"""
		Запись информации в текстовый файл.

		:return: Ничего.
		"""
		text = self.__str__()
		with open('file.txt', 'w') as f:
			f.write(text)
			f.close()

	def __len__(self):
		"""
		Подсчёт количества докторов в больнице.

		:return: Количество докторов.
		:rtype: int
		"""
		return len(self.__doctors)

	def __getitem__(self, item):
		"""
		Получение доктора/медсестры по индексу.

		:param item: Индекс.
		:type item: int
		:raises IndexError: Доктор/медсестра не был(-а) найден(-а) в больнице.
		:return: Найденного(-ую) доктора/медсестру.
		:rtype: Person
		"""
		if item == 0:
			s = ""
			for n in self.__nurses:
				s += n.__str__() + "\n"
			return s
		else:
			try:
				return self.__doctors[item - 1]
			except IndexError:
				print("Invalid index")

	def __delitem__(self, item):
		"""
		Удаление доктора/медсестры по индексу.

		:param item: Индекс.
		:type item: int
		:raises KeyError: Доктор/медсестра не был(-а) найден(-а) в больнице.
		:return: Найденного(-ую) доктора/медсестру.
		:rtype: Person
		"""
		if item == 0:
			return self.__nurses.clear()
		else:
			try:
				return self.__doctors.pop(item - 1)
			except KeyError:
				return "Invalid index"

	def __setitem__(self, key, value):
		"""
		Прикрепление доктора к больнице.

		:param key: Ключ.
		:type key: int
		:param value: Значение.
		:type value: Doctor
		:raises KeyError: Неверный ключ.
		:return: None
		"""
		if key == 0:
			return None
		try:
			self.__doctors[key - 1] = value
		except KeyError:
			print("Invalid enter")

	def __add__(self, other):
		"""
		Добавление медсестры в больницу.

		:param other: Медсестра.
		:type other: Nurse
		:return: Добавленная медсестра.
		:rtype: Nurse
		"""
		return self.__nurses.append(other)

	def __sub__(self, other):
		"""
		Удаление медсестры из больницы.

		:param other: Медсестра.
		:type other: Nurse
		:return: Удалённая медсестра.
		:rtype: Nurse
		"""
		for i in range(len(self.__nurses)):
			if self.__nurses[i].__str__() == other.__str__():
				return self.__nurses.pop(i)
		return self.__nurses

	def __str__(self):
		"""
		Приведение объекта класса к строке.

		:return: Свойства класса.
		:rtype: str
		"""
		s = "Hospital: {}\nAddress: {}\nDoctors:".format(str(self.__name), str(self.__address))
		for docs in self.__doctors:
			s += docs.__str__() + "\n"
		s += "\nNurses:"
		for nurs in self.__nurses:
			s += nurs.__str__() + "\n"
		return s
