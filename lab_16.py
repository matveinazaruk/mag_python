def x_range( *args):
	if len(args) == 1:
		start, stop, step = 0, args[0], 1
	elif len(args) == 2:
		start, stop, step = args[0], args[1], 1
	elif len(args) == 3:
		start, stop, step = args
	else:
		raise TypeError('xrange() requires 1-3 int arguments')

	current = start
	while (step > 0 and current < stop) or (step < 0 and current > stop):
		yield current
		current += step

assert list(x_range(1, 5, 2)) == list(range(1, 5, 2))
assert list(x_range(5, 1, -2)) == list(range(5, 1, -2))
assert list(x_range(1, 5)) == list(range(1, 5))
assert list(x_range(5)) == list(range(5))
