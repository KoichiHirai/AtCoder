# https://atcoder.jp/contests/abc173/tasks/abc173_a

n = int(input())
print(0) if n % 1000 == 0 else print(1000 - (n % 1000))