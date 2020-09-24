import random

def cfg(name, rules):
    if isinstance(name, tuple):
        return cfg(random.choice(name), rules)
    if isinstance(name, list):
        return "".join([cfg(x, rules) for x in name])
    if name in rules:
        return cfg(rules[name], rules)
    else:
        return name

def test(rules, n):
    print("".join([cfg("S", rules) + "\n" for i in range(n)]))

g1 = {
    "S": ["T", ("S", ("T", ""))],
	"T": ("1", "0")
}

g2 = {
	"S": ["(", ("", "S"), ")"]
}

g3 = {
	"S": ("BR", [("x", "y"), "OPERATION"]),
	"BR": ["(", [("x", "y"), "OPERATION"], ")", ("", "OPERATION")],
	"OPERATION": ("ADD", "SUB", "MUL", "DIV"),
	"ADD": [" + ", (("x", "y"), "BR")],
	"SUB": [" - ", (("x", "y"), "BR")],
	"MUL": [" * ", (("x", "y"), "BR")],
	"DIV": [" / ", (("x", "y"), "BR")]
}


test(g3, 10)