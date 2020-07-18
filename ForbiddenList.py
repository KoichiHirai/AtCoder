# https://atcoder.jp/contests/abc170/tasks/abc170_c
x,n = map(int,input().split())

if n == 0:
	print(x)
	exit()

value = []
for i in range(1,100):
	value.append(i)

for i in input().split():
	value.remove(int(i))

left = 0
right = len(value)

while right - left > 1:
	mid = (left + right) // 2
	if value[mid] > x:
		right = mid
	else:
		left = mid
if x - value[right-1] <= value[right] - x:
	print(value[right-1])
else:
	print(value[right])