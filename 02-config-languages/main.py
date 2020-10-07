from sys import argv
from calclex import CalcLexer
from calcpars import CalcParser


def file_path():
    data = ""
    f = open(argv[1], "r")
    for row in f:
        data += row
    return data


def manual():
    return '''
        (groups
            (
                "ИКБО-1-19"
                "ИКБО-2-19"
                "ИКБО-3-19"
                "ИКБО-4-19"
                "ИКБО-5-19"
                "ИКБО-6-19"
                "ИКБО-7-19"
                "ИКБО-8-19"
                "ИКБО-9-19"
                "ИКБО-10-19"
                "ИКБО-11-19"
                "ИКБО-12-19"
                "ИКБО-13-19"
                "ИКБО-14-19"
                "ИКБО-15-19"
                "ИКБО-16-19"
                "ИКБО-17-19"
                "ИКБО-18-19"
                "ИКБО-19-19"
                "ИКБО-20-19"
                "ИКБО-21-19"
                "ИКБО-22-19"
                "ИКБО-23-19"
                "ИКБО-24-19"
                "ИКБО-25-19"
            )
        students
            (
                (
                    (age 19) (group "ИКБО-4-19") (name "Иванов И.И.")
                )
                (
                    (age 18) (group "ИКБО-5-19") (name "Петров П.П.")
                )
                (
                    (age 18) (group "ИКБО-5-19") (name "Сидоров С.С.")
                )
                (
                    (age 19) (group "ИКБО-1-19") (name "Акимов В.Е.")
                )
            )
        subject "Конфигурационное управление"
        )
'''


if __name__ == "__main__":
    CalcParser.do_pars(file_path())





'''
Примеры выводов парсера (для тестирования)

(
    (
        (
            'groups',
                ['"ИКБО-1-19"', '"ИКБО-2-19"', '"ИКБО-3-19"']
        ),
        (
            'students',
            [
                [('age', 19), ('group', '"ИКБО-1-19"'), ('name', '"Иванов И.И."')],
                [('age', 20), ('group', '"ИКБО-3-19"'), ('name', '"Петров П.П."')],
                [('age', 19), ('group', '"ИКБО-2-19"'), ('name', '"Олегов О.О."')]
            ]
        )
    ),
    ('subject', '"Конфигурационное управление"')
)




(
    (
        'groups',
            ['"ИКБО-1-19"', '"ИКБО-2-19"', '"ИКБО-3-19"']
    ),
    (
        (
            'students',
            [
                [('age', 19), ('group', '"ИКБО-1-19"'), ('name', '"Иванов И.И."')],
                [('age', 20), ('group', '"ИКБО-3-19"'), ('name', '"Петров П.П."')],
                [('age', 19), ('group', '"ИКБО-2-19"'), ('name', '"Олегов О.О."')]
            ]
        ),
        (
            'subject', '"Конфигурационное управление"'
        )
    )
)




(
    [
        'groups',
            ['"ИКБО-1-19"', '"ИКБО-2-19"', '"ИКБО-3-19"']
    ],
    [
        'students',
        [
            [('age', 19), ('group', '"ИКБО-1-19"'), ('name', '"Иванов И.И."')],
            [('age', 20), ('group', '"ИКБО-3-19"'), ('name', '"Петров П.П."')],
            [('age', 19), ('group', '"ИКБО-2-19"'), ('name', '"Олегов О.О."')]
        ],
        ('subject', '"Конфигурационное управление"')
    ]
)


(
    [
        'groups',
            ['"ИКБО-1-19"', '"ИКБО-2-19"', '"ИКБО-3-19"']
    ],
    [
        'students',
            [
                [('age', 19), ('group', '"ИКБО-1-19"'), ('name', '"Иванов И.И."')],
                [('age', 20), ('group', '"ИКБО-3-19"'), ('name', '"Петров П.П."')],
                [('age', 19), ('group', '"ИКБО-2-19"'), ('name', '"Олегов О.О."')]
            ]
    ],
    (
        'subject', '"Конфигурационное управление"'
    )
)




[
    [
        'groups',
            ['"ИКБО-1-19"', '"ИКБО-2-19"', '"ИКБО-3-19"']
    ],
    [
        'students',
            [
                [('age', 19), ('group', '"ИКБО-1-19"'), ('name', '"Иванов И.И."')],
                [('age', 20), ('group', '"ИКБО-3-19"'), ('name', '"Петров П.П."')],
                [('age', 19), ('group', '"ИКБО-2-19"'), ('name', '"Олегов О.О."')]
            ]
    ],
    ('subject', '"Конфигурационное управление"')
]



[
    'groups',
        ['"ИКБО-1-19"', '"ИКБО-2-19"', '"ИКБО-3-19"'],
    'students',
        [
            [('age', 19), ('group', '"ИКБО-1-19"'), ('name', '"Иванов И.И."')],
            [('age', 20), ('group', '"ИКБО-3-19"'), ('name', '"Петров П.П."')],
            [('age', 19), ('group', '"ИКБО-2-19"'), ('name', '"Олегов О.О."')]
        ],
    ('subject', '"Конфигурационное управление"')
]
'''
