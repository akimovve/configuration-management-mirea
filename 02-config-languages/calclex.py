from sly import Lexer


class CalcLexer(Lexer):
    # Токены, необходимые для лексического разбора
    tokens = {NUMBER, VAR, STRING}

    # Литералы (скобки)
    literals = {"(", ")"}

    # Игнорируемые элементы (пробел/табуляция, комментарий, след. строка)
    ignore = " \t"
    ignore_comment = r"\#.*"
    ignore_newline = r"\n+"

    # Правила в виде рег. выражений для токенов
    NUMBER = r"\d+"
    VAR = r"[a-z]+\d*"
    STRING = r"(\"|\').*?(\"|\')"

    # Конвертация типов для каждого из токенов
    def NUMBER(self, c):
        c.value = int(c.value)
        return c

    def VAR(self, c):
        c.value = str(c.value)
        return c

    def STRING(self, c):
        c.value = str(c.value)
        return c

    def ignore_newline(self, c):
        self.lineno += c.value.count("\n")

    def error(self, c):
        print("Line %d: Bad character %r" % (self.lineno, c.value[0]))
        self.index += 1

    @staticmethod
    def do_lex(data):
        lexer = CalcLexer()
        for tok in lexer.tokenize(data):
            print(tok)
