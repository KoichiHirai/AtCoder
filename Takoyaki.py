# https://atcoder.jp/contests/abc176/tasks/abc176_a

n,x,t = map(int,input().split())

print(n//x*t) if n % x == 0 else print((n//x+1)*t) 