def x_range( *args):
	if len(args) == 1:
		start, stop, step = 0, args[0], 1
	elif len(args) == 2:
		start, stop, step = args[0], args[1], 1
	elif len(args) == 3:
		start, stop, step = args
	else:
		raise TypeError('x_range() requires 1-3 int arguments')

	if step == 0:
		raise ValueError('x_range() arg 3 must not be zero')

	current = start
	while (step > 0 and current < stop) or (step < 0 and current > stop):
		yield current
		current += step

#Correct
assert list(x_range(1, 5, 2)) == list(range(1, 5, 2))
assert list(x_range(1, 5, -2)) == list(range(1, 5, -2))
assert list(x_range(1, 5)) == list(range(1, 5))
assert list(x_range(5)) == list(range(5))

#Incorrect
assert list(x_range(1, 5, -2)) == list(range(1, 5, -2))
assert list(x_range(5, 1)) == list(range(5, 1))
