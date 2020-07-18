# https://atcoder.jp/contests/abc161/tasks/abc161_c

n,k = (int(x) for x in input().split())

if n == 0 or k == 1 or n == k:
	print(0)
	exit()

if n < k:
	print(n) if n < k - n else print(k-n)
else :
	mod = n % k 
	print(mod) if mod < k - mod else print(k-mod)