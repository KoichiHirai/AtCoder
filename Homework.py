# https://atcoder.jp/contests/abc163/tasks/abc163_b

n,m = map(int,input().split())
a = list(map(int,input().split()))
for i in range(m):
	n -= a[i]
	if n < 0:
		print(-1)
		exit()
print(n)