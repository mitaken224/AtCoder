N = int(input())
S = N * (N + 1) // 2

x = N
i = 1
while x >= 10:
    if x < 100:
        S -= (10 ** i - 1) * (N - (10 ** i - 1))
        break
    else:
        S -= (10 ** i - 1) * ((10 ** (i + 1) - 1) - (10 ** i - 1))
        x /= 10
        i += 1

S %= 998244353

print(S)