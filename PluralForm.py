# https://atcoder.jp/contests/abc179/tasks/abc179_a

s = input()
print (s + "es") if s[len(s)-1] == "s" else print(s + "s")