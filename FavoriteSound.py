# https://atcoder.jp/contests/abc120/tasks/abc120_a

input = input().split()

intInput = [int(i) for i in input]

result = 0

#満足してしまうとき
if(intInput[0]*intInput[2] <= intInput[1]):
	print(intInput[2])
#一回も聞けないとき
elif(intInput[0]>intInput[1]):
	print(0)
#満足できないとき
else:
	for i in range(intInput[2]):
		result = result + intInput[0]
		if(intInput[1] - result < intInput[0]):
			print(i+1)
			break


# print(intInput[2])