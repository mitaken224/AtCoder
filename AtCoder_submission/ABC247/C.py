N = int(input())
S = ["1"]

for i in range(2, N + 1):
    add_S = S[:]
    S.append(str(i))
    for s in add_S:
        S.append(s)

print(" ".join(S))