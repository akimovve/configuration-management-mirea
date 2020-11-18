import sys
import inspect
import calc
import random


def coverage(f):
	lines = set()

	def trace(frame, event, arg):
		lines.add((event, frame.f_lineno))
		return trace

	sys.settrace(trace)
	f()
	sys.settrace(None)
	return lines


def print_coverage(module, trace):
	lines = [y for x, y in trace]
	source = inspect.getsource(module).splitlines()
	for i, x in enumerate(source):
		print(("|" if i + 1 in lines else " ") + x)


def test_calc(s):
	try:
		return calc.calc(s)
	except:
		pass


def tests():
	for _ in range(10000):
		test_calc(gen())


def gen():
	a = "+-*/"
	b = "()"
	return " ".join([" ".join(["".join([str(random.choice(range(9)))
										for _ in range(random.choice(range(1, 5)))]),
							random.choice(a), random.choice(b)])
					for _ in range(random.choice(range(5)))])


c = coverage(tests)
print_coverage(calc, c)
print(len(c))
