# https://atcoder.jp/contests/agc024/tasks/agc024_a
result = [0] * 3
a,b,c,k = map(int, input().split())

for i in range(k):
	result[0] = b + c
	result[1] = a + c
	result[2] = a + b

	a = result[0]
	b = result[1]
	c = result[2]

print("Unfair") if a-b > 10**18 else print(a-b)