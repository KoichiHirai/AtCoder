# https://atcoder.jp/contests/abc126/tasks/abc126_a

n,k = map(int,input().split())
s = list(input())

s[k-1] = s[k-1].lower()

print(''.join(s))