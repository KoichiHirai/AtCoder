# https://atcoder.jp/contests/abc083/tasks/abc083_b
answer = 0
n,a,b = map(int,input().split())
for i in range(1,n+1):
	sum_i = 0 
	str_i = str(i)
	for j in range(len(str_i)):
		sum_i += int(str_i[j])
	if sum_i >= a and sum_i <= b:
		answer += i
print(answer)