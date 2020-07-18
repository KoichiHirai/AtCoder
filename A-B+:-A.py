# https://atcoder.jp/contests/abc118/tasks/abc118_a

a,b = (int(x) for x in input().split())

print(a + b if b % a == 0 else b - a)