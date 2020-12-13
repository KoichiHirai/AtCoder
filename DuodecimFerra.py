# https://atcoder.jp/contests/abc185/tasks/abc185_c
l = int(input())
up,down = l-1,1
for i in range(2,12):
	up *= l-i
	down *= i
print(int(up/down))