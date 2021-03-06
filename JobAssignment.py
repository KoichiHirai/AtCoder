# https://atcoder.jp/contests/abc194/tasks/abc194_b
n = int(input())
first_a, second_a, first_b, second_b, min_sum = 10001,10001,10001,10001,10001
index_a, index_b = 0,0
for i in range(n):
	a,b = map(int,input().split())
	if first_a > a:
		second_a = first_a
		first_a = a
		index_a = i
	elif second_a > a:
		second_a = a
	if first_b > b:
		second_b = first_b
		first_b = b
		index_b = i
	elif second_b > b:
		second_b = b
	min_sum = min(min_sum,a+b)
if index_a == index_b:
	print(min(min(max(first_a,second_b),max(second_a,first_b)),min_sum))
else:
	print(min(max(first_a,first_b),min_sum))