# https://atcoder.jp/contests/abc182/tasks/abc182_a
a,b = map(int,input().split())
followNumber = 2 * a + 100
print(0) if  followNumber < b else print(followNumber - b)