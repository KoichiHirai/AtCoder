# https://atcoder.jp/contests/abc124/tasks/abc124_c
s = input()
odd,even = 0,0
len_s = len(s)
len_even = len_s // 2
len_odd = len_s - len_even

for i in range(len_s):
	if i % 2 == 0 and s[i] == "1":
		odd += 1
	elif i % 2 == 1 and s[i] == "1":
		even += 1

print((len_even-even)+odd) if (len_even-even)+odd < even+(len_odd-odd)  else print(even+(len_odd-odd))
