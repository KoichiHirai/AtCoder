# https://atcoder.jp/contests/abc062/tasks/abc062_b
pixel = []
h,w = map(int,input().split())
for i in range(h):
	pixel.append(input())
print("#"*(w+2))
for i in range(h):
	print("#" + pixel[i] + "#")
print("#"*(w+2))