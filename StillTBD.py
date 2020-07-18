# https://atcoder.jp/contests/abc119/tasks/abc119_a
import datetime

input = input()

date = datetime.datetime.strptime(input, "%Y/%m/%d")

if date <= datetime.datetime(2019, 4, 30):
	print("Heisei")
else:
	print("TBD")

# print(date)