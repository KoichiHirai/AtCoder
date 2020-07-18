input = input().split()

intList = [int(i) for i in input]

result = intList[2]

for i in range(10):
	result = intList[0] * result - intList[1] 
	print(result)