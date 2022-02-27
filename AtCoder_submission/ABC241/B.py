N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

flg = True

for i in range(M):
    if B[i] in A:
        A.remove(B[i])
    else:
        flg = False
        break

if flg:
    print("Yes")
else:
    print("No")