# https://atcoder.jp/contests/abc144/tasks/abc144_a

a,b = map(int,input().split())

print(-1) if a > 9 or b > 9 else print(a*b)