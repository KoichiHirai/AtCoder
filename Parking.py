# https://atcoder.jp/contests/abc080/tasks/abc080_a
n,a,b = map(int,input().split())
print(n*a) if n*a < b else print(b) 