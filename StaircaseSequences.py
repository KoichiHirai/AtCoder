# https://atcoder.jp/contests/abc190/tasks/abc190_d
n = int(input())
answer = 0
count = 1
minus = 0
while(True):
	if minus >= n:
		break
	if (n-minus)%count == 0:
		answer += 2 
	minus = minus+count
	count += 1
print(answer)