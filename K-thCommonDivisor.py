# https://atcoder.jp/contests/abc120/tasks/abc120_b

input = input().split()

intInput = [int(i) for i in input]

# 割る最大数を決定
division = min(intInput[0],intInput[1])

# 公約数を入れるリスト
list=[1]

# 2以上の数で割っていき、intInput[0]とintInput[1]の両方割り切れたら、iをリストに追加 
for i in range(2, division+1):
	if intInput[0] % i == 0 and intInput[1] % i == 0:
		list.append(i)

print(list[len(list)-intInput[2]])

# print(list)