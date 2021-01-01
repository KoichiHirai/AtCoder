# https://atcoder.jp/contests/abc103/tasks/abc103_b
s = list(input())
t = list(input())
len_string = len(s)
string = s
for i in range(len_string):
	if t == string:
		print("Yes")
		exit()
	else:
		s = string
		string = ["0"] * len_string
		string[0] = s[-1]
		for j in range(0,len_string-1):
			string[j+1] = s[j]
print("No")