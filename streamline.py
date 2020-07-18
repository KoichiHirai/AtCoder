# https://atcoder.jp/contests/abc117/tasks/abc117_b

n,m = (int(i) for i in input().split())
x = [int(i) for i in input().split()]

if n >= m:
	print(0)
else:
	sorted_x = sorted(x)
 
	diff_x = []
	diff = 0
	result = 0
 
	for i in range(m-1):
		diff = sorted_x[i+1] - sorted_x[i]
		result += diff
		diff_x.append(diff)

	sorted_diff = sorted(diff_x, reverse=True)[:n-1]
 
	for i in range(n-1):
		result -= sorted_diff[i]
	 
	print(result)	