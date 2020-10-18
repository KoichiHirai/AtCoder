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
	for i in numbers:
		print(i)

# a,b,k = map(int,input().split())
# numbers = list(range(a,b+1))
# for i in range(k):
# 	print(numbers[i])
# for i in range(max(k+1, len(numbers)-k),len(numbers)):
# 	print(numbers[i])