a = 1
i = 1
for i in range(20):
	b = a % 3
	c = a % 5
	d = a % 15
	if d == 0:
		print("fizzbuzz")

	elif b == 0:
		print("fizz")

	elif c == 0:
		print("buzz")

	else:
		print(a)
	
	a = a + 1
