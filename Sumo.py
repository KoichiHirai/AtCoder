# https://atcoder.jp/contests/m-solutions2019/tasks/m_solutions2019_b
s = input()

win = s.count("o")

number = len(s)

print("YES" if win + (15 - number) >= 8 else "NO")