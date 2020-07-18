s = int(input())
k = int(input())

if s // 10 == 0:
	print(s)
else:
	listInt = [int(x) for x in list(str(s))]
	for i in range(len(listInt)):
		print(listInt)
		if listInt[i] == 1:
			if listInt[i] > k:
				print("a")
				print(listint[i])
				break
		else:
			if listInt[i] ** ((5 * 10 ** 15) - 1) > k:
				print("b")
				print(listint[i])
				break
		k -= listInt[i] ** ((5 * 10 ** 15) - 1)
print("c")