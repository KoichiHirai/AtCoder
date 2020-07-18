# https://atcoder.jp/contests/abc117/tasks/abc117_b

n = int(input())
l = [int(x) for x in input().split()]

max_index = l.index(max(l))

sum_length = 0

for x in range(n):
	if x == max_index:
		continue
	sum_length += l[x]

print ("Yes") if sum_length > max(l) else print ("No")