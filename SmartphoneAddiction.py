# https://atcoder.jp/contests/abc185/tasks/abc185_b
n,m,t = map(int,input().split())
time = 0
battery = n
for i in range(m):
	a,b = map(int,input().split())
	battery -= (a-time)
	if battery <= 0:
		print("No")
		exit()
	battery += (b-a)
	if n < battery:
		battery = n
	time = b
battery -= (t-time)
if battery <= 0:
	print("No")
	exit()
print("Yes")