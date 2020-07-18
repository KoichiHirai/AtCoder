# https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_c
a,b,c = (int(x) for x in input().split())
print("Yes") if 4*a*b < (c-a-b)**2 and c-a-b > 0 else print("No")