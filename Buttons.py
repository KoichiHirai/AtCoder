# https://atcoder.jp/contests/abc124/tasks/abc124_a

a,b = map(int,input().split())
answer = 0
for i in range(2):
	if a > b:
		answer += a
		a -= 1
	else: 
		answer += b
		b -= 1
print(answer)