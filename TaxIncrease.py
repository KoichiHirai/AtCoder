# https://atcoder.jp/contests/abc158/tasks/abc158_c

a,b = map(int,input().split())

for i in range(1,1010):
	if int(i*0.08) == a and int(i*0.1) == b:
		print(i)
		exit()
print(-1)