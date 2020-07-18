# https://atcoder.jp/contests/abc157/tasks/abc157_c

n,m = (int(i) for i in input().split())
number = [0] * n
number[0] = 1
numberFlag = [0] * n
answer = ""
if m == 0 and n == 1:
	print(0)
	exit(0)
elif m > 0:
	for i in range(m):
		s,c = (int (i) for i in input().split())
		if s == 1 and c == 0 and n > 1:
			print(-1)
			exit(0)
		elif number[s-1] != c and numberFlag[s-1] == 1:
			print(-1)
			exit(0)
		elif numberFlag[s-1] == 0:
			number[s-1] = c
			numberFlag[s-1] = 1

for i in range(n):
	answer += str(number[i])
print(answer)



