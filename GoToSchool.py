# https://atcoder.jp/contests/abc142/tasks/abc142_c

n = int(input())
a = list(map(int,input().split()))
answer = []

for i in range(1,n+1):
	print(a.index(i)+1, end = " ")