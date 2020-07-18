# https://atcoder.jp/contests/abc137/tasks/abc137_b

k,x = (int(x) for x in input().split())

length = k * 2 - 1

if x - k < -1000000:
	firstNo = -1000000
elif x + k > 1000000:
	firstNo = 1000000 - length + 1
else:
	firstNo = x - k + 1
for i in range(length):
	print(str(firstNo + i) + " ", end = "")

