# https://atcoder.jp/contests/abc072/tasks/abc072_a
X,t = map(int,input().split())
print(0) if X-t < 0 else print(X-t)