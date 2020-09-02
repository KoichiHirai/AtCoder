# https://atcoder.jp/contests/abc165/tasks/abc165_b

x = int(input())
year = 0
deposit = 100

while(deposit < x):
	year += 1
	deposit += int(deposit/100)

print(year)