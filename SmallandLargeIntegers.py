# https://atcoder.jp/contests/abc093/tasks/abc093_b

a,b,k = map(int,input().split())
length = b-a+1
numbers = list(range(a,b+1))
if length > k * 2:
	for i in range(k*2):
		if i < k:
			print(numbers[i])
		else:
			print(numbers[i-k*2])
else:
	for i in range(length):
		print(numbers[i])