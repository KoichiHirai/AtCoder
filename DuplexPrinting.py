# https://atcoder.jp/contests/abc157/tasks/abc157_a
n = int(input())

q, mod = divmod(n, 2)

print(q + mod)