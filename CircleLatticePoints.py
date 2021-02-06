# https://atcoder.jp/contests/abc191/tasks/abc191_d
import math
x,y,r = map(float,input().split())
min_x = math.ceil(x-r)
max_x = math.floor(x+r)
min_y = math.ceil(y-r)
max_y = math.floor(y+r)
answer = (max_x-min_x+1)*(max_y-min_y+1)
# print("min_x:" + str(min_x) + "max_x: " + str(max_x))
# print("min_y:" + str(min_y) + "max_x: " + str(max_y))

if math.sqrt((min_x-x)**2+(min_y-y)**2) > r:
	answer -= 1
if math.sqrt((min_x-x)**2+(max_y-y)**2) > r:
	answer -= 1
if math.sqrt((max_x-x)**2+(min_y-y)**2) > r:
	answer -= 1
if math.sqrt((max_x-x)**2+(max_y-y)**2) > r:
	answer -= 1

print(answer)
