# https://atcoder.jp/contests/abc079/tasks/abc079_a
n = input()
print("Yes") if (n[0] == n[1] and n[1] == n[2]) or (n[1] == n[2] and n[2] == n[3]) else print("No")