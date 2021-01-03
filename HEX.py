# https://atcoder.jp/contests/abc078/tasks/abc078_a
A,B,C,D,E,F = 10,11,12,13,14,15
x,y = input().split()
if eval(x) > eval(y):
	print(">")
elif eval(x) == eval(y):
	print("=")
else:
	print("<")