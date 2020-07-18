# https://atcoder.jp/contests/abc127/tasks/abc127_d

n,m = (int(x) for x in input().split())
card = [int(x) for x in input().split()]
max_b = 0
max_c = 0

for i in range(m):
	b,c = (int(x) for x in input().split())
	if max_b > b and max_c > c:
		continue
	if max_b < b:
		max_b = b
	if max_c < c:
		max_c = c

	for x in range(b):
		if min(card) < c:
			card[card.index(min(card))] = c 
		else:
			break
print(sum(card))

			