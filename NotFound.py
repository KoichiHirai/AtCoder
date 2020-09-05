# https://atcoder.jp/contests/abc071/tasks/abc071_b

s = input()

for i in range(97,123):
	if not chr(i) in s:
		print(chr(i))
		exit()

print("None")