# https://atcoder.jp/contests/abc126/tasks/abc126_b
s = input()

first = int(s[:2])
second = int(s[2:])

firstFlag = 0
secondFlag = 0

if first > 12 or first < 1:
	firstFlag = 1

if second > 12 or second < 1:
	secondFlag = 1

if firstFlag == 0:
	if secondFlag == 0:
		print("AMBIGUOUS")
	else:
		print("MMYY")
elif firstFlag == 1:
	if secondFlag == 0:
		print("YYMM")
	else:
		print("NA")