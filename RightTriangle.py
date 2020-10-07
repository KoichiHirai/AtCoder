# https://atcoder.jp/contests/abc116/tasks/abc116_a

abc = list(map(int,input().split()))
abc.remove(max(abc))
print(int(abc[0] * abc[1] / 2))