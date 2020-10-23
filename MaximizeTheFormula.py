# https://atcoder.jp/contests/abc110/tasks/abc110_a
numbers = list(map(int,input().split()))
numbers.sort()
print(int(str(numbers[2]) + str(numbers[1])) + numbers[0])