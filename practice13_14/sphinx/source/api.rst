Руководство разработчика
========================

Модуль main для запуска программы и тестирования работоспособности классов, написанных на языке программирования `Python <https://www.python.org>`_.

.. automodule:: main
	:members:

Классы
#######

Ниже представлен класс-родитель Person, от которого унаследованы остальные классы, описанные далее.

.. automodule:: Person

.. autoclass:: Person
	:members:
	:inherited-members:

	.. automethod:: __init__
	.. automethod:: __str__

График наследования классов
###########################
Наследование классов Doctor и Nurse от Person.

.. inheritance-diagram:: Doctor
.. inheritance-diagram:: Nurse

Классы, наследованные от Person
###############################
**Класс Doctor.**

.. automodule:: Doctor

.. autoclass:: Doctor
	:members:

	.. automethod:: __init__
	.. automethod:: __str__


**Класс Nurse.**

.. automodule:: Nurse

.. autoclass:: Nurse
	:members:

	.. automethod:: __init__
	.. automethod:: __str__


**Класс Hospital**, объединяющий в себе все вышеописанные объекты классов.

.. automodule:: Hospital

.. autoclass:: Hospital
	:members:

	.. automethod:: __init__
	.. automethod:: __len__
	.. automethod:: __getitem__
	.. automethod:: __delitem__
	.. automethod:: __setitem__
	.. automethod:: __add__
	.. automethod:: __sub__
	.. automethod:: __str__