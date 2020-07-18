# https://atcoder.jp/contests/abc160/tasks/abc160_c
k,n = (int(x) for x in input().split())
a = [int(x) for x in input().split()]

diff = 0
largest_diff = 0
sumNum = 0 

for x in range(n-1):
	diff = a[x+1]-a[x]
	sumNum += diff
	if largest_diff < diff:
		 largest_diff = diff

last_diff = k-a[n-1]+a[0]
sumNum += last_diff
if largest_diff < last_diff:
	largest_diff = last_diff

print(sumNum-largest_diff)