n = int(input())

if n < 105:
	print(0)
elif n == 105 or n == 106:
	print(1)
else:
	if n % 2 == 0:
		length = int(n / 2) - 1
	else:
		length = int(n / 2)
	array = []
	answer = 1
	for i in range(53,length+1):
		number = i * 2 + 1
		for x in range(1,n+1):
			if number % x == 0:
				array.append(x)
		if len(array) == 8:
			answer += 1
		array.clear()
	print(answer)