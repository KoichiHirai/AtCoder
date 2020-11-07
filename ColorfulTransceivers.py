# https://atcoder.jp/contests/abc097/tasks/abc097_a
a,b,c,d = map(int,input().split())
print("Yes") if (d >= abs(c-a)) or (d >= abs(b-a) and d >= abs(c-b)) else print("No")