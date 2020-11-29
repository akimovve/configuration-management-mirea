from Doctor import Doctor
from Nurse import Nurse
from Hospital import Hospital


def doctor_test():
	"""
	Тестирование работоспособности класса Doctor

	:return: Статус выполнения операций
	:rtype: bool
	"""
	doc1 = Doctor("Mark", "Timber", 56, 16443, "Dentist")
	doc1.add_patient(991, "Pavel Globov")
	doc1.add_patient(423, "Gigi Lin")
	doc1.add_patient(437, "Pavel Globov")
	doc1.add_patient(717, "Matt Pirson")
	doc1.print_patients()
	doc1.remove_patient("Pavel Globov")

	doc2 = Doctor("Jeremy", "Martin", 39, 11841, "Dentist")
	doc2.add_patient(387, "Nick Jim")
	doc2.add_patient(109, "Andrew Yolk")

	doc3 = Doctor("Jack", "Fern", 70, 98612, "Ent")
	doc3.add_patient(238, "Olga Fern")
	doc3.add_patient(619, "Gosha Shilk")

	print(doc1)
	doc1.print_patients()
	print(doc2)
	doc2.print_patients()
	print(doc3)
	doc3.print_patients()
	return True


def nurse_test():
	"""
	Тестирование работоспособности класса Nurse

	:return: Статус выполнения операций
	:rtype: bool
	"""
	nur1 = Nurse("Mary", "Colber", 29, 81751, "Dentistry")
	nur1.add_schedule("Monday", "09.00 am - 06.00 pm")
	nur1.add_schedule("Wednesday", "09.00 am - 07.00 pm")
	nur1.add_schedule("Friday", "09.00 am - 06.30 pm")
	nur1.add_schedule("Saturday", "10.30 am - 05.30 pm")
	nur1.add_schedule("Sunday", "12.30 am - 10.00 pm")
	nur1.print_schedule()
	nur1.remove_schedule("Saturday")
	nur1.print_schedule()
	nur1.add_schedule("Monday", "08.00 am - 09.00 pm")
	nur1.change_schedule("Tuesday", "09.00 am - 06.00 pm")
	nur1.change_schedule("Monday", "07.00 am - 02.00 pm")
	nur1.print_schedule()
	print(nur1)
	nur1.change_dep("new Dentistry")
	print(nur1)
	return True


def hospital_test():
	"""
	Тестирование работоспособности класса Hospital

	:return: Статус выполнения операций
	:rtype: bool
	"""
	hos = Hospital("Invitro", "Wall Str.")

	doc1 = Doctor("Jeremy", "Martin", 39, 11841, "Dentist")
	doc2 = Doctor("Peter", "Petrov", 26, 18674, "Ent")
	doc3 = Doctor("Ulan", "Bator", 86, 74381, "Pediatrician")

	hos.add_doctor(doc1)
	hos.add_doctor(doc2)
	hos.add_doctor(doc3)

	doc1.add_patient(173, "Martin Garrix")

	doc2.add_patient(808, "McRon Dam")

	doc3.add_patient(717, "Will Smith")
	doc3.add_patient(111, "Migel Jewer")

	nur1 = Nurse("Kira", "Syrok", 21, 87123, "Dentistry")
	nur2 = Nurse("Mary", "Chris", 18, 51972, "Psyche")
	nur3 = Nurse("Olga", "Brain", 27, 98547, "Dentistry")

	hos.add_nurse(nur1)
	hos.add_nurse(nur2)
	hos.add_nurse(nur3)

	nur1.add_schedule("Friday", "06.00 am - 10.30 pm")

	nur2.add_schedule("Tuesday", "09.30 am - 06.30 pm")
	nur2.add_schedule("Sunday", "09.30 am - 09.30 pm")

	nur3.add_schedule("Wednesday", "10.00 am - 04.30 pm")

	hos + Nurse("Michele", "Wild", 26, 20817, "Psyche")
	hos - Nurse("Kira", "Syrok", 21, 87123, "Dentistry")
	hos - Nurse("Margaret", "Readl", 31, 83710, "Stud")
	hos + Nurse("Liza", "Smigline", 19, 10293, "Dentistry")

	print(hos)
	print("------------")
	print("Doctors number:", len(hos))
	print("------------")
	print(hos[0])
	print("------------")
	print(hos[1])
	print("------------")
	print(hos[15])
	del hos[2]
	print(hos)
	hos.create_txt()
	return True


def main():
	"""
	Функция main. Запускает функции проверки описанных классов.

	:return: Ничего не возвращает
	"""
	doctor_test()
	nurse_test()
	hospital_test()
