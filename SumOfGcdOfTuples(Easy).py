# https://atcoder.jp/contests/abc162/tasks/abc162_c
import itertools

k = int(input())
k_list = list(range(1,k+1))
h_list = list(itertools.combinations_with_replacement(k_list, 3))
answer = 0
max_value = 0
print(h_list)

for item in h_list:
	print(item)
	m_item = min(item)
	for i in range(1, m_item+1):
		if  item[0] % i == 0 and item[1] % i == 0 and item[2] % i == 0:
			max_value = i
	if item.count(item[0]) == 3:
		answer += max_value
		print(max_value)
	else:
		answer += (max_value * 3)
		print(max_value * 3)

print(answer)