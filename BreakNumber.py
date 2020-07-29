# https://atcoder.jp/contests/abc068/tasks/abc068_b

n = int(input())
result = 0
while(2 ** result < n):
	result += 1
print(2 ** result)