# https://atcoder.jp/contests/abc137/tasks/abc137_c
import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n = int(input())

listStr = [list(input()) for i in range(n)]
listFullStr = []

for i in range(n):
	fullStr = ""
	listStr[i].sort()
	for x in listStr[i]:
		fullStr += x
	listFullStr.append(fullStr)

answer = 0
while(True):
	firstStr = listFullStr[0]
	count = listFullStr.count(firstStr)
	if count != 1:
		answer = answer + combinations_count(count, 2)
	for firstStr in listFullStr:
		listFullStr.remove(firstStr)
	if len(listFullStr) == 0:
		break;

print(answer)