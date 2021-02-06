# https://atcoder.jp/contests/abc191/tasks/abc191_a
v,t,s,d = map(int,input().split())
start = t * v
end = s * v
print("No") if start <= d and d <= end else print("Yes")