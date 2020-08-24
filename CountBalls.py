# https://atcoder.jp/contests/abc158/tasks/abc158_b

n,a,b = map(int,input().split())
answer = 0

while(True):
	if n <= a:
		answer += n
		break
	if n < a + b:
		answer += a
		break
	answer += a
	n -= (a + b)
print(answer)