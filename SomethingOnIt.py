# https://atcoder.jp/contests/abc095/tasks/abc095_a
s = input()
topping = 0
for i in range(3):
	if s[i] == "o":
		topping += 1
print(700 + topping * 100)