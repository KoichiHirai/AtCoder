# https://atcoder.jp/contests/cf17-relay-open/tasks/relay2_c

w = []
d = []
n,k = map(int,input().split())
for i in range(n):
	w1,d1 = map(int,input().split())
	w.append(w1)
	d.append(d1)

range_min = 0
range_max = 2 * 10 ** 18

while abs(range_max - range_min) > 1:
	mid = (range_max + range_min) // 2

	sum_flowers = 0
	for i in range(n):
		if mid >= w[i]:
			sum_flowers +=  (mid - w[i]) // d[i] + 1

	if sum_flowers < k:
		range_min = mid 
	else:
		range_max = mid

print(range_max)