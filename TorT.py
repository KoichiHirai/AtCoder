# https://atcoder.jp/contests/abc133/tasks/abc133_a

n,a,b = map(int,input().split())
print(a * n) if a * n < b else print(b)