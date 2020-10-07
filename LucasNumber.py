# https://atcoder.jp/contests/abc079/tasks/abc079_b

n = int(input())
luca = [0] * (n+1)
luca[0] = 2
luca[1] = 1
for i in range(2,n+1):
	luca[i] = luca[i-1] + luca[i-2]
print(luca[n])