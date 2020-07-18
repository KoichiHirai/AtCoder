# https://atcoder.jp/contests/dwacon6th-prelims/tasks/dwacon6th_prelims_a
n = int(input())
songs = []
for i in range(n):
	songs.append(input().split())
x = input()

for j in range(n):
	if songs[j][0] == x:
		break

answer = 0

for i in range(j+1,n):
	answer += int(songs[i][1])

print(answer)