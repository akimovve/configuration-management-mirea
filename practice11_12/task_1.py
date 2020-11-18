def unique_elements(lst):
	"""
	Docs.
	>>> unique_elements([1, 2, 3, 4, 4, 1, 0, 1])
	5
	>>> unique_elements([]) is None
	True
	>>> unique_elements([4, 4, 4, 4])
	1
	"""
	if lst:
		return len(set(lst))
	return None


def test_unique_elements():
	assert (unique_elements([1, 2, 3, 4, 4, 1, 0, 1])) == 5
	assert (unique_elements([])) is None
	assert (unique_elements([4, 4, 4, 4])) == 1
