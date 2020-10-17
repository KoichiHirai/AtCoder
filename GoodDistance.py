# https://atcoder.jp/contests/abc133/tasks/abc133_b
import math
n,d = map(int,input().split())
dots = []
answer = 0
for i in range(n):
	dots.append(list(map(int,input().split())))
for i in range(n):
	for j in range(i+1,n):
		result = 0
		for k in range(d):
			result += (dots[i][k] - dots[j][k])**2
		if math.sqrt(result).is_integer():
			answer += 1
print(answer)