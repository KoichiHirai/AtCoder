# https://atcoder.jp/contests/abc190/tasks/abc190_b
n,s,d = map(int,input().split())
damage = 0
for i in range(n):
	x,y = map(int,input().split())
	if x < s and d < y:
		damage = 1
print("Yes") if damage == 1 else print("No")