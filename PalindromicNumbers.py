# https://atcoder.jp/contests/abc090/tasks/abc090_b

a,b = map(int,input().split())
count = 0
for i in range(a,b+1):
	str_i = str(i)
	if str_i[0] == str_i[4] and str_i[1] == str_i[3]:
		count += 1
print(count)