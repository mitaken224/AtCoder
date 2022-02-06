import math

N = int(input())

N_log = math.log(N, 10)
S = sum(range(1, N + 1))

for i in range(1, int(N_log) + 1):
    if N_log < i + 1:
        S -= (10 ** i - 1) * (N - (10 ** i - 1))
    else:
        S -= (10 ** i - 1) * ((10 ** (i + 1) - 1) - (10 ** i - 1))

S %= 998244353

print(S)