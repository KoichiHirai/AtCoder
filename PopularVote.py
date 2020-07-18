# https://atcoder.jp/contests/abc161/tasks/abc161_b
n,m = (int(x) for x in input().split())
a = [int(x) for x in input().split()]



popular = 0
sumVote = sum(a)
q,mod = divmod(sumVote,4*m)

if(mod == 0):
	line = q - 1
else:
	line = q

if(q < 1):
	print("Yes")
	exit()

for x in range(n):
	if(a[x] > line):
		popular += 1 
	if(popular == m):
		print("Yes")
		exit()

print("No")
