N, K, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if A[i] >= X:
        if K >= A[i] // X:
            K -= A[i] // X
            A[i] = A[i] % X
        else:
            A[i] -= K * X
            K = 0
    if K == 0:
        print(sum(A))
        exit()
        
A.sort(reverse=True)

for i in range(N):
    A[i] = 0
    K -= 1
    
    if K == 0:
        break

print(sum(A))