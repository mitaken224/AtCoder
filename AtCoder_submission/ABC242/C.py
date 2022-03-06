N = int(input())
X = [[0] * 9 for i in range(N)]

for j in range(9):
    X[0][j] += 1

for i in range(1, N):
    for j in range(9):
        for k in range(max(0, j - 1), min(9, j + 2)):
            X[i][k] += X[i - 1][j]
            X[i][k] %= 998244353

sum = 0
for j in range(9):
    sum += X[N - 1][j]
    sum %= 998244353
print(sum)