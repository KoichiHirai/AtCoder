# https://atcoder.jp/contests/abc139/tasks/abc139_a

s = list(input())
t = list(input())

answer = 0

for i in range(3):
	if s[i] == t[i]:
		answer+=1

print(answer)

