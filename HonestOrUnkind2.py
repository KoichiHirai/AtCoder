# https://atcoder.jp/contests/abc147/tasks/
# 入力を一旦回答に寄せて考えたほうがいい

n = int(input())

list_a = []
testimonies = []
answer = 0
flag = True

for i in range(n):
	testimony = []
	a = int(input())
	list_a.append(a)
	for j in range(a):
		testimony.append(list(map(int,input().split())))
	testimonies.append(testimony)

for i in range(1 << n): # 部分和の計算　i=2は"0b10"  正直者の組み合わせの全パターン
	result = 0
	for j in range(n): # 各正直者の組み合わせを確認
		if i & (1 << (j)): #trueだった場合はj番目は正直者
			result += 1
			for k in range(list_a[j]): #正直者の証言を確認
				if not i ^ (testimonies[j][k][1] << testimonies[j][k][0]-1): # 虚偽の証言をしている時
					flag = False
					break
			# if flag == False:
			# 	break
	if flag == True:
		if answer < result:
			answer = result
	else:
		flag = True
	

# for i in range(1 << (n-1)): # 部分和の計算　i=2は"0b10" 
# 	result = 0
# 	for j in range(n): # 各桁を確認 jは桁数を表す
# 		if i & (1 << (j)): #trueだった場合はj桁目は1である(後ろからj番目は正直者)
# 			for k in range(list_a[-j]):
# 				if i & testimonies[-j][k][1] << (testimonies[-j][k][0]-1):
# 					flag = False
# 					break
# 			if flag == True:
# 				result += 1
# 			else:
# 				flag = True
# 	if answer < result:
# 		answer = result

print(answer)