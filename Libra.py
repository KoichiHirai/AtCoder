# https://atcoder.jp/contests/abc083/tasks/abc083_a
a,b,c,d = map(int,input().split())
l,r = a+b, c+d
if l > r:
	print("Left")
elif l == r:
	print("Balanced")
else:
	print("Right")