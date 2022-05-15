N = int(input())
O = set()
Champ_score = 0
Champ_number = 0

for i in range(N):
    S, T = input().split()
    T = int(T)
    if S not in O:
        O.add(S)
        if T > Champ_score:
            Champ_score = T
            Champ_number = i + 1

print(Champ_number)