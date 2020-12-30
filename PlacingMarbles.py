# https://atcoder.jp/contests/abc081/tasks/abc081_a
s = input()
answer = 0
for i in range(3):
	if s[i] == "1":
		answer += 1
print(answer)