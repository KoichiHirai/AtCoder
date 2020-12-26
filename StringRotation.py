# https://atcoder.jp/contests/abc103/tasks/abc103_b
s = list(input())
t = list(input())
len_string = len(s)
string = ["a"] * len_string
for i in range(len_string-1):
	string[0] = t[-1]
	for j in range(0,len_string-1):
		string[i+1] = t[j]
	print("string: " + str(string))
	if s == string:
		print("Yes")
		exit()
	else:
		t = string
		string = ["a"] * len_string
print("No")