X, A, D, N = map(int, input().split())

S = []
for i in range(N):
    S.append(A + D * i)

min = float('inf')
for s in S:
    dist = abs(X - s)
    if min > dist:
        min = dist

print(min)