# https://atcoder.jp/contests/abc042/tasks/arc058_a

n,k = (int(x) for x in input().split())
d = [int(x) for x in input().split()]

num = [int(x) for x in list(str(n))]

if not num[len(num)-1] in d:
	for i in range(num[len(num)-1]+1,9):
		if i in d:
			num[len(num)-1] = i
			break
		if i == 9:
			n += 1
			num = [int(x) for x in list(str(n))]

answer = ""

for i in range(len(num)):
	if not num[i] in d:
		answer += str(num[i])
	else:
		for x in range(i+1,9):
			if x in d:
				answer += str(x)
				break
				
print(answer)