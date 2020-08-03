# https://atcoder.jp/contests/abc155/tasks/abc155_a

a,b,c = map(int,input().split())

print("Yes") if (a == b or b == c or c == a) and not(a == b and b == c and c == a) else print("No")