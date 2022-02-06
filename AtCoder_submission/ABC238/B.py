N = int(input())
A = list(map(int, input().split(" ")))
P = []

for i in range(N):
    P.append(A[i])
    for j in range(i):
        P[j] += A[i]

for i in range(N):
    P[i] %= 360

P = sorted(P)

max = P[0]
for i in range(1, N):
    diff = P[i] - P[i - 1]
    if diff > max:
        max = diff

diff = 360 - P[-1]    
if  diff > max:
    max = diff

print(max)