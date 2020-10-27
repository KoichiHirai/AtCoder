# https://atcoder.jp/contests/abc103/tasks/abc103_a
a = list(map(int,input().split()))
a.sort()
print((a[2]-a[1]) + (a[1]-a[0]) )
