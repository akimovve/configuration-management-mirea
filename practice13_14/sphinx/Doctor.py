from Person import Person


class Doctor(Person):
	"""
	Модель (класс) доктор.
	"""

	def __init__(self, name, family_name, age, id_number, speciality):
		"""
		Конструктор класса доктор.

		:param name: Имя доктора.
		:type name: str
		:param family_name: Фамилия доктора.
		:type family_name: str
		:param age: Возраст доктора.
		:type age: int
		:param id_number: Идентификационный номер доктора.
		:type id_number: int
		:param speciality: Специальность доктора.
		:type speciality: str
		"""
		Person.__init__(self, name, family_name, age)
		self.__id_number = id_number
		self.__speciality = speciality
		self.__patients = {}

	def add_patient(self, new_patient_id, new_patient_name):
		"""
		Добавление пациента доктору.

		:param new_patient_id: Идентификационный номер пациента.
		:type new_patient_id: int
		:param new_patient_name: Имя пациента.
		:type new_patient_name: str
		:return: Информация о добавлении пациента.
		:rtype: str
		"""
		self.__patients[new_patient_id] = new_patient_name
		print("New patient {} added".format(new_patient_name))

	def remove_patient(self, written_out_patient):
		"""
		Удаление пациента из записи к доктору.

		:param written_out_patient: Имя пациента.
		:type written_out_patient: str
		:return: Информацию об удалении пациента.
		:rtype: str
		"""
		same_names = 0
		pat_id = 0
		for key, value in self.__patients.items():
			if value == written_out_patient:
				same_names += 1
				pat_id = key
		if same_names == 0:
			print("{} was not found".format(written_out_patient))
		elif same_names == 1:
			print("{} was written out".format(self.__patients.pop(pat_id)))
		else:
			pat_id = int(input("\nThere are 2 similar patients. Enter the id: "))
			try:
				print("{} was written out".format(self.__patients.pop(pat_id)))
			except KeyError:
				print("{} with id {} was not found".format(written_out_patient, pat_id))

	def print_patients(self):
		"""
		Печать всех пациентов доктора в консоль.

		:return: Список пациентов
		:rtype: str
		"""
		s = ""
		for key, value in self.__patients.items():
			s += "\t{0}: {1}\t".format(key, value)
		print(s)
		if not s:
			return "\tNo patients"
		return s

	def __str__(self):
		"""
		Приведение объекта класса к строке.

		:return: Свойства класса.
		:rtype: str
		"""
		s = "\tSpeciality: {}\n\tID: {}\nPatients:\n{}" \
			.format(str(self.__speciality),
					str(self.__id_number),
					str(self.print_patients()))
		return super(Doctor, self).__str__() + s
