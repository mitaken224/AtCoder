N = int(input())
S = input()
L = []
R = []

for i in range(N):
    if S[i] == "L":
        R.append(str(i))    # R.append(i)
    else:
        L.append(str(i))    # L.append(i)

print(" ".join(L + [str(N)] + R[::-1])) # print(*(L + [N] + R[::-1])