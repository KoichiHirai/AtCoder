# https://atcoder.jp/contests/abc166/tasks/abc166_b

n,k = (int(i) for i in input().split())

belongs = [0] * n

for i in range(k):
	if 0 in belongs:
		d = int(input())
		a = [int(j) for j in input().split()]
		for j in range(d):
			belongs[a[j]-1] = 1

print(belongs.count(0))