# https://atcoder.jp/contests/abc108/tasks/abc108_a

k = int(input())

even = k // 2
odd = k // 2 if k % 2 == 0 else (k + 1) // 2

print(even * odd)