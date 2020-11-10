# https://atcoder.jp/contests/abc104/tasks/abc104_b
s =  input()
len_s = len(s)
position_c = 0
count_c = 0

if s[0] != "A":
	print("WA")
	exit()

for i in range(2,len_s-1):
	if s[i] == "C":
		count_c += 1
		if count_c == 1:
			position_c = i
	if count_c != 1 :
		print("WA")
		exit()	

for i in range(len_s):
	if i == 0 or i == position_c:
		continue
	else:
		if s[i].isupper():
			print(s[i])
			print("WA")
			exit()

print("AC")