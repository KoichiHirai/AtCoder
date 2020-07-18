# https://atcoder.jp/contests/abc160/tasks/abc160_b
x = int(input())
ans = 0
q,mod = divmod(x,500)
ans += q * 1000
q,mod = divmod(mod,5)
ans += q * 5
print(ans)