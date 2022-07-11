import string

N, X = map(int, input().split())
S = ""

for s in string.ascii_uppercase:
    for i in range(N):
        S += s

print(S[X - 1])