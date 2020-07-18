# https://atcoder.jp/contests/abc162/tasks/abc162_b
n = int(input())
sum = 0
for i in range(1,n+1):
	if i % 3 == 0 or i % 5 == 0:
		continue
	sum += i 
print(sum)
