# https://atcoder.jp/contests/abc160/tasks/abc160_a
s = input()

s_list = list(s)

print("Yes") if s_list[2] == s_list[3] and s_list[4] == s_list[5] else print("No")