# https://atcoder.jp/contests/abc092/tasks/abc092_b]

n = int(input())
d,x = map(int,input().split())

for i in range(n):
	a = int(input())
	x += ((d - 1) // a) + 1

print(x)