# https://atcoder.jp/contests/abc118/tasks/abc118_b

n,m = (int(x) for x in input().split())

foods = []
for a in range(m):
	foods.append(0)

for i in range(n):
	answer = [int(x) for x in input().split()]
	for x in range(1,answer[0]+1):
		foods[answer[x]-1] += 1

print(foods.count(n))