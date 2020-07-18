# https://atcoder.jp/contests/abc128/tasks/abc128_b

from operator import itemgetter

number = int(input())

listInput = [input() for i in range(number)]

record = []

for i in range(len(listInput)):
	tumple = listInput[i].split()
	record.append((tumple[0], int(tumple[1]), i + 1))

sort1 = sorted(record, key = itemgetter(1), reverse = True)
sort2 = sorted(sort1, key = itemgetter(0))

for a,b,c in sort2:
	print(c)