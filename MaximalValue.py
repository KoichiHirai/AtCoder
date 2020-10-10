# https://atcoder.jp/contests/abc140/tasks/abc140_c

answer = []
n = int(input())
b = list(map(int,input().split()))
answer.append(b[0])

for i in range(1,n-1):
	answer.append(b[i-1]) if b[i-1] < b[i] else answer.append(b[i])
answer.append(b[n-2])
print(sum(answer))