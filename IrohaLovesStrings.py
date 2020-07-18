# https://atcoder.jp/contests/abc042/tasks/abc042_b

n,l = (int(x) for x in input().split())

s = [input() for x in range(n)]

s.sort()
answer = ""

for i in range(len(s)):
	answer += s[i]

print(answer)