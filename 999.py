# https://atcoder.jp/contests/abc111/tasks/abc111_a

n = input()

print(n.translate(str.maketrans({"1":"9", "9":"1"})))