# https://atcoder.jp/contests/abc109/tasks/abc109_b

n = int(input())
w = [input()]
answer = "Yes"
for i in range(1,n):
	input_w = input()
	if answer == "No":
		w.append(input_w)
		continue
	elif w[i-1][len(w[i-1])-1] != input_w[0] or input_w in w:
		answer = "No"
	w.append(input_w)
print(answer)