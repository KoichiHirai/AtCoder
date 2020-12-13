# https://atcoder.jp/contests/abc185/tasks/abc185_d
answer = 0
n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
diff = []
for i in range(m-1):
	diff.append(a[i+1]-a[i])
diff_min = min(diff)
for i in diff:
	if i // diff_min == 0:
		answer += i // diff_min
	else:
		answer += (i // diff_min) + 1
print(answer)