# https://atcoder.jp/contests/abc127/tasks/abc127_c

n,m = (int(x) for x in input().split())
l,r = (int(x) for x in input().split())

for i in range(m - 1):
	a,b = (int (x) for x in input().split())
	if l > r:
		continue
	if l < a:
		l = a
	if r > b:
		r = b

print(r - l + 1 if r >= l else 0)

