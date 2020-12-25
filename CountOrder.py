# https://atcoder.jp/contests/abc150/tasks/abc150_c
n = int(input())
order = [1,1]

for h in range(2):
	pq = list(map(int,input().split()))
	numbers = list(range(1,n+1))
	for i in range(n):
		for j in range(len(numbers)):
			if pq[i] == numbers[j]: 
				order[h] *= j
				numbers.remove(numbers[j])

print(abs(order[1]-order[1]))
