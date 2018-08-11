def memoize(f):
	cache = {}

	def decorate(*args):
		if args in cache:
			return cache[args]
		else:
			cache[args] = f(*args)
			return cache[args]

	return decorate


@memoize
def fibonacci(n):
	if n in [0, 1]:
		return n
	return fibonacci(n - 1) + fibonacci(n - 2)
