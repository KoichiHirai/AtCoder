# https://atcoder.jp/contests/abc113/tasks/abc113_b
n = int(input())
t,a = (int(x) for x in input().split())
h = [int(x) for x in input().split()]

best = t - h[0] * 0.006
ans = 0

for i in range(1,n):
	tem = t - h[i] * 0.006
	if abs(a - tem) < abs(a - best):
		best = tem
		ans = i
print(ans + 1)