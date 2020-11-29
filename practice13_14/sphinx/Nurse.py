from Person import Person


class Nurse(Person):
	"""
	Модель (класс) медсестра.
	"""

	def __init__(self, name, family_name, age, id_number, work_dep):
		"""
		Конструктор класса медсестра.

		:param name: Имя медсестры.
		:type name: str
		:param family_name: Фамилия медсестры.
		:type family_name: str
		:param age: Возраст медсестры.
		:type age: int
		:param id_number: Идентификационный номер медсестры.
		:type id_number: int
		:param work_dep: Отделение работы медсестры.
		:type work_dep: str
		"""
		Person.__init__(self, name, family_name, age)
		self.__id_number = id_number
		self.__work_dep = work_dep
		self.__schedule = {}

	def change_dep(self, new_work_dep):
		"""
		Перевод медсетры в другое отделение.

		:param new_work_dep: Новое отделение.
		:type new_work_dep: str
		:return: Ничего.
		"""
		self.__work_dep = new_work_dep

	def add_schedule(self, week_day, hours):
		"""
		Добавление расписания медсестре.

		:param week_day: Рабочий день недели.
		:type week_day: str
		:param hours: Рабочие часы.
		:type hours: str
		:return: Информацию об установке расписания.
		:rtype: str
		"""
		if week_day in self.__schedule.keys():
			print("Schedule already exists")
		else:
			self.__schedule[week_day] = hours
		print("New schedule added")

	def remove_schedule(self, week_day):
		"""
		Удаление расписания медсестры.

		:param week_day: День недели для удаления.
		:type week_day: str
		:return: Информацию об удалении расписания.
		:rtype: str
		"""
		try:
			del self.__schedule[week_day]
			print("{} was deleted".format(week_day))
		except KeyError:
			print("{} was not found".format(week_day))

	def change_schedule(self, week_day, hours):
		"""
		Изменение расписания медсестры.

		:param week_day: День недели для изменения.
		:type week_day: str
		:param hours: Рабочие часы.
		:type hours: str
		:return: Информацию об изменении расписания.
		:rtype: str
		"""
		if week_day in self.__schedule.keys():
			self.__schedule[week_day] = hours
			print("Schedule was changed")
		else:
			print("Schedule was not found")

	def print_schedule(self):
		"""
		Печать расписания медсестры.

		:return: Расписание.
		:rtype: str
		"""
		s = ""
		for key, value in self.__schedule.items():
			s += "\t{0}: {1}\n".format(key, value)
		print(s)
		if not s:
			return "\tNo schedule"
		return s

	def __str__(self):
		"""
		Приведение объекта класса к строке.

		:return: Свойства класса.
		:rtype: str
		"""
		s = "\tWork Department: {}\n\tID: {}\nSchedule:\n{}" \
			.format(str(self.__work_dep),
					str(self.__id_number),
					str(self.print_schedule()))
		return super(Nurse, self).__str__() + s
