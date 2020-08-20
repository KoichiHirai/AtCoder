# https://atcoder.jp/contests/abc175/tasks/abc175_a

s = list(input())
result = 0
answer = 0

for i in range(len(s)):
	if s[i] == "R":
		result += 1
	else:
		result = 0
	if result > answer:
		answer = result

print(answer) 