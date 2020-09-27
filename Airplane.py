# https://atcoder.jp/contests/abc129/tasks/abc129_a

pqr = list(map(int,input().split()))
pqr.remove(max(pqr))
print(sum(pqr))