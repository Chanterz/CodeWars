def tribonacci(signature, n):
	a, b, c = signature

	if n == 0:
		return []
	if n <= 3:
		return signature[:n]

	for _ in range(n - 3):
		a, b, c = b, c, a + b + c
		signature.append(c)
	return signature


print(tribonacci([1, 1, 1], 1))
