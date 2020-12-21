# https://atcoder.jp/contests/abc104/tasks/abc104_b

s = input()

if s[0] != "A":
	print("WA")
	exit()

position_C = s.find("C") 
if position_C == -1 or position_C == 1 or position_C == len(s)-1:
	print("WA")
	exit()

s_list = list(s)
s_list.remove("A")
s_list.remove("C") 


for i in s_list:
	if i.islower() == False:
		print("WA")
		exit()

print("AC")