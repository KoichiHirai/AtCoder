# https://atcoder.jp/contests/abc182/tasks/abc182_b
n = int(input())
a = list(map(int, input().split()))
answer,answerNumber,maxNumber = 0,0,0

for i in range(2,max(a)+1):
	for j in range(n):
		if a[j] % i == 0:
			maxNumber += 1
	if answerNumber < maxNumber:
		answerNumber = maxNumber
		answer = i
	maxNumber = 0

print(answer)