# https://atcoder.jp/contests/abc105/tasks/abc105_a
n,k = map(int,input().split())
print(0) if n % k == 0 else print(1)