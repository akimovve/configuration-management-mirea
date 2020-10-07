from sly import Parser
from calclex import CalcLexer
from jsonmaker import JSONMaker as js


class CalcParser(Parser):
    # Токены из класса для лексического разбора
    tokens = CalcLexer.tokens

    @_("'(' expr_set ')'")
    def response(self, p):
        return p.expr_set

    @_("expr_set expr_set")
    def expr_set(self, p):
        return p.expr_set0 + p.expr_set1

    @_("expr '(' expr_list ')'")
    def expr_set(self, p):
        return [p.expr, p.expr_list]

    @_("expr_list STRING")
    def expr_list(self, p):
        p.expr_list.append(p.STRING)
        return p.expr_list

    @_("STRING STRING")
    def expr_list(self, p):
        return [p.STRING0, p.STRING1]

    @_("expr_list NUMBER")
    def expr_list(self, p):
        p.expr_list.append(p.STRING)
        return p.expr_list

    @_("NUMBER NUMBER")
    def expr_list(self, p):
        return [p.STRING0, p.STRING1]

    @_("expr '(' objects ')'")
    def expr_set(self, p):
        return [p.expr, p.objects]

    @_("objects '(' object ')'")
    def objects(self, p):
        p.objects.append(p.object)
        return p.objects

    @_("'(' object ')' '(' object ')'")
    def objects(self, p):
        return [p.object0, p.object1]

    @_("object '(' param ')'")
    def object(self, p):
        p.object.append(p.param)
        return p.object

    @_("'(' param ')' '(' param ')'")
    def object(self, p):
        return [p.param0, p.param1]

    @_("expr NUMBER")
    def param(self, p):
        return p.expr, p.NUMBER

    @_("expr STRING")
    def param(self, p):
        return p.expr, p.STRING

    @_("expr_set param")
    def expr_set(self, p):
        p.expr_set.append(p.param)
        return p.expr_set

    @_("STRING")
    def expr(self, p):
        return p.STRING

    @_("NUMBER")
    def expr(self, p):
        return p.NUMBER

    @_("VAR")
    def expr(self, p):
        return p.VAR

    @staticmethod
    def do_pars(data):
        lexer = CalcLexer()
        parser = CalcParser()
        try:
            js.print_json(parser.parse(lexer.tokenize(data)))
        except EOFError:
            print("Error in creating result")


'''
БНФ

response    | (expr_set)

expr_set    | expr_set expr_set
expr_set    | expr (expr_list)
expr_set    | expr (objects)
expr_set    | expr_set param

objects     | objects (object)

object      | object (param)
object      | (param) (param)

expr_list   | expr_list STRING
expr_list   | expr_list NUMBER
expr_list   | STRING STRING
expr_list   | NUMBER NUMBER

param       | expr STRING
param       | expr NUMBER

expr        | STRING
expr        | NUMBER
expr        | VAR

'''
