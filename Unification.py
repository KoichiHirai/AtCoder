# https://atcoder.jp/contests/abc120/tasks/abc120_c

input = input()

listInt = [int(i) for i in input]

index = 0
result = 0

while len(listInt) != index + 1:
	if listInt[index] != listInt[index+1]:
		# print ("a index: ", end='')
		# print(index)
		# print(listInt)
		listInt.pop(index)
		listInt.pop(index)
		index = index - 1 
		result = result + 2
		if(len(listInt) == 0): 
			break
		continue		
	index = index + 1
print(result)

