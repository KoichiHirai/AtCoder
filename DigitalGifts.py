# https://atcoder.jp/contests/abc119/tasks/abc119_b
number = int(input())

input = [input() for i in range(number)]

result = 0

for i in range(number):
	otoshidama = input[i].split()
	if otoshidama[1] == "JPY":
		result = result + float(otoshidama[0])
	elif otoshidama[1] == "BTC":
		result = result + float(otoshidama[0]) * 380000.0

print(result)	