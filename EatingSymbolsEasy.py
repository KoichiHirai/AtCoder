# https://atcoder.jp/contests/abc101/tasks/abc101_a
s = input()
answer = 0
for i in range(4):
	if s[i] == "+":
		answer += 1
	else:
		answer -= 1
print(answer)