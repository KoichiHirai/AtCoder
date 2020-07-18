# https://atcoder.jp/contests/abc148/tasks/abc148_a
numbers = [1, 2, 3]
a = int(input())
b = int(input())

numbers.remove(a)
numbers.remove(b)

print(numbers[0])