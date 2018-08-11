def get_divisors(num):
	result = []
	for i in range(1, num + 1):
		if num / i - num // i == 0:
			result.append(i)
	return result


def get_sum_squared_list(lst):
	return sum([x ** 2 for x in lst])


def list_squared(m, n):
	res = [[x, sum(map(lambda x: x * x, get_divisors(x)))] for x in range(m, n + 1) if
	       sum(map(lambda x: x * x, get_divisors(x))) - int(sum(map(lambda x: x * x, get_divisors(x)))) == 0]
	return res


print(list_squared(1, 250))
