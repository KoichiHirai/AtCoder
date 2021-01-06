# https://atcoder.jp/contests/abc187/tasks/abc187_a
a,b = input().split()
sa = int(a[0]) + int(a[1]) + int(a[2])
sb = int(b[0]) + int(b[1]) + int(b[2])
print(sa) if sa > sb else print(sb)