# https://atcoder.jp/contests/abc139/tasks/abc139_c
n = int(input())
h = list(map(int,input().split()))
answer,count = 0,0
for i in range(n-1):
	if h[i] >= h[i+1]:
		count += 1
		if answer < count:
			answer = count
	else:
		count = 0
print(answer)