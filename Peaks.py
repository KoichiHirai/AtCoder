# https://atcoder.jp/contests/abc166/tasks/abc166_c

n,m = (int(i) for i in input().split())
h = [int(i) for i in input().split()]
maxTower = [1] * n # 他の展望台と比べて、低かったら0を立てる

for i in range(m):
	a,b = (int(j) for j in input().split())
	if h[a-1] == h[b-1]:
		maxTower[a-1] = 0
		maxTower[b-1] = 0
	elif h[a-1] < h[b-1]:
		maxTower[a-1] = 0
	else:
		maxTower[b-1] = 0

print(maxTower.count(1))