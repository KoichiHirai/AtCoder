# https://atcoder.jp/contests/abc190/tasks/abc190_a
a,b,c = map(int,input().split())
if a < b:
	print("Aoki")
elif a > b:
	print("Takahashi")
else:
	if c == 0:
		print("Aoki")
	else:
		print("Takahashi")