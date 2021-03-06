# https://atcoder.jp/contests/abc194/tasks/abc194_c
n = int(input())
a = list(map(int,input().split()))
answer = 0
for i in range(1 << n):
	numbers = []
	for j in range(n):
		if (i & (1 << j)):
			numbers.append(a[j])
	if len(numbers) == 2:
		answer += (numbers[0]- numbers[1])**2
print(answer)