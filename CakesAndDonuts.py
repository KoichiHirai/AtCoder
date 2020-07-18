a = int(input())

if a == 3 or a == 6 or a == 9:
	print("No")
elif a % 4 == 0 or a % 3 == 0:
	print("Yes")
else:
	a = a - (a // 4) * 4
	if a == 0:
		print("Yes")
	else:
		a = a - (a // 3) * 3
		if a == 0:
			print("Yes")
		else:
			print("No") 


# for i in range(100):
# 	a = i
# 	if a == 3 or a == 6 or a == 9:
# 		print(str(i) + "= No")
# 	elif a % 4 == 0 or a % 7 == 0:
# 		print(str(i) + "= Yes")
# 	else:
# 		a = a - (a // 4) * 4
# 		if a == 0:
# 			print(str(i) + "= Yes")
# 		else:
# 			a = a - (a // 3) * 3
# 			if a == 0:
# 				print(str(i) + "= Yes")
# 			else:
# 				print(str(i) + "= No") 
		