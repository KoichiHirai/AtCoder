# https://atcoder.jp/contests/abc142/tasks/abc142_c

n = int(input())
a = list(map(int,input().split()))
answer = [0] * n

for i in range(n):
	answer[a[i]-1] = i + 1 

for i in range(n):
	print(answer[i], end = " ")