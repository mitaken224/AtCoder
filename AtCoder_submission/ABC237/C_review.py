S = input()
N = len(S)

x = 0
for i in range(N):
    if S[i] == "a":
        x += 1
    else:
        break

y = 0
for i in range(N):
    if S[N - 1 - i] == "a":
        y += 1
    else:
        break

if x == N:
    print("Yes")
elif x > y:
    print("No")
else:
    S = "a" * (y - x) + S
    
    if S == S[::-1]:
        print("Yes")
    else:
        print("No")