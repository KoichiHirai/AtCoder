# https://atcoder.jp/contests/abc141/tasks/abc141_c

n,k,q = map(int,input().split())
points = [0] * n
for i in range(q):
	points[int(input())-1] += 1

for i in range(n):
	print("Yes") if k - q + points[i] > 0 else print("No")