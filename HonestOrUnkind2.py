# https://atcoder.jp/contests/abc147/tasks/abc147_c

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

for i in range(1 << n): # 部分和の計算　i=2は"0b10" 
	result = 0
	for j in range(n): # 各桁を確認 jは桁数を表す
		if i & (1 << (j)): #trueだった場合はj桁目は1である(後ろからj番目は正直者)
			for k in range(list_a[-j]):
				if i & testimonies[-j][k][1] << (testimonies[-j][k][0]-1):
					flag = False
					break
			if flag == True:
				result += 1
			else:
				flag = True
	if answer < result:
		answer = result

print(answer)