# https://atcoder.jp/contests/abc152/tasks/abc152_b
a,b = map(int,input().split())
print(str(a) * b) if a < b else print(str(b) * a)