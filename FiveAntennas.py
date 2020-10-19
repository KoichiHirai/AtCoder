# https://atcoder.jp/contests/abc123/tasks/abc123_a
antennas = []
for i in range(5):
	antennas.append(int(input()))
k = int(input())
print(":(") if k < antennas[4] - antennas[0] else print("Yay!")