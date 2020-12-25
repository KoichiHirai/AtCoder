# https://atcoder.jp/contests/abc050/tasks/abc050_b
p = []
x = [] 
n = int(input())
t = list(map(int,input().split()))
m = int(input())
for i in range(m):
	px = list(map(int,input().split()))
	p.append(px[0])
	x.append(px[1])
t_sum = sum(t)
for i in range(m):
	print(t_sum - t[p[i]-1] + x[i])