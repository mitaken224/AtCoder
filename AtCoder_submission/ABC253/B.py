from posixpath import split


H, W = map(int, input().split())
o_num = 0

for i in range(H):
    S = input()
    for j in range(len(S)):
        if S[j] == "o":
            if o_num == 0:
                start = [i, j]
            if o_num == 1:
                goal = [i, j]
            if o_num >= 2:
                break

            o_num += 1

print(abs(start[0] - goal[0]) + abs(start[1] - goal[1]))