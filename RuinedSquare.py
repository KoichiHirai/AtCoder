# https://atcoder.jp/contests/abc108/tasks/abc108_b

x1,y1,x2,y2 = (int(x) for x in input().split())

x = x2 - x1
y = y2 - y1

x3 = x2 - y
y3 = y2 + x

x4 = x3 - x
y4 = y3 - y

print(str(x3) + " " + str(y3) + " " + str(x4) + " " + str(y4))