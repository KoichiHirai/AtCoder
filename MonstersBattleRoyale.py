# https://atcoder.jp/contests/abc118/tasks/abc118_c

n = input()

monster = [int(x) for x in input().split()]

while(True):
	minIndex = monster.index(min(monster))
	for i in range(len(monster)): 
		if i == minIndex or monster[i] == 0:
			continue
		if monster[i] % monster[minIndex] == 0:
			monster[i] = 0
		else:
			monster[i] -= monster[minIndex] * (monster[i]//monster[minIndex])
	monster = [x for x in monster if x != 0]
	if len(monster) == 1:
		print(monster[0])
		break