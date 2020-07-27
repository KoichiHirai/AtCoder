# https://atcoder.jp/contests/abc086/tasks/abc086_b

import math
a,b = input().split()
number = int(a + b)
# print(number)
# print(math.sqrt(number))
# print((math.sqrt(number))**2

sqrtNumber = math.sqrt(number)

print("Yes") if int(sqrtNumber) == sqrtNumber else print("No")