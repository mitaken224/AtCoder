H, W = map(int, input().split(" "))

A = []

for i in range(H):
    A_i = list(map(int, input().split(" ")))
    A.append(A_i)

for i in range(W):
    B_i = []
    for j in range(H):
        B_i.append(str(A[j][i]))
    print(' '.join(B_i))