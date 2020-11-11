# https://atcoder.jp/contests/abc094/tasks/abc094_a
a,b,x = map(int,input().split())
print("NO") if x < a or x - a > b else print("YES")