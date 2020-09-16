# https://atcoder.jp/contests/abc136/tasks/abc136_a

a,b,c = map(int,input().split())
print(0) if c-(a-b) < 0 else print(c-(a-b))