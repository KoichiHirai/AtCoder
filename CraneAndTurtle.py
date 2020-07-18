# https://atcoder.jp/contests/abc170/tasks/abc170_b

x,y = map(int,input().split())

if y % 2 == 1:
	print("No")
	exit()

diff = y - x * 2

if diff < 0 or diff // 2 > x:
	print("No")
else:
	print("Yes")