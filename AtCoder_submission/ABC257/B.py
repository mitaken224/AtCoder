N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for l in L:
    if A[l - 1] == N:
        continue
    elif (A[l - 1] + 1) in A:
        continue
    else:
        A[l - 1] += 1

A = map(str, A)
print(" ".join(A))