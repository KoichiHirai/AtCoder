# https://atcoder.jp/contests/abc153/tasks/abc153_a

h,a = map(int,input().split())
print(h//a) if h % a == 0 else print((h//a)+1)