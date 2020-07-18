# https://atcoder.jp/contests/abc157/tasks/abc157_b
a = [int(i) for i in input().split()]
for i in range(2):
	a.extend([int(i) for i in input().split()])
# print(a)
n = int(input())
b = []
for i in range(n):
	# b.append(int(input()))
	b = int(input())
	if b in a:
		a[a.index(b)] = 0
if a.count(0) < 3:
	print("No")		
elif a[0] == 0 and a[1] == 0 and a[2] == 0:
	print("Yes")
elif a[3] == 0 and a[4] == 0 and a[5] == 0:
	print("Yes")
elif a[6] == 0 and a[7] == 0 and a[8] == 0:
	print("Yes")
elif a[0] == 0 and a[3] == 0 and a[6] == 0:
	print("Yes")
elif a[1] == 0 and a[4] == 0 and a[7] == 0:
	print("Yes")
elif a[2] == 0 and a[5] == 0 and a[8] == 0:
	print("Yes")
elif a[0] == 0 and a[4] == 0 and a[8] == 0:
	print("Yes")
elif a[2] == 0 and a[4] == 0 and a[6] == 0:
	print("Yes")
else:
	print("No")