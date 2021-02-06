# https://atcoder.jp/contests/abc191/tasks/abc191_b
n,x = map(int,input().split())
a = list(map(int,input().split()))
for i in range(n):
	if a[i] != x:
		print(a[i], end=" ")