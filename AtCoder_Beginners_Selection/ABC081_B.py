N = int(input())
A_i = list(map(int, input().split()))

cnt = 0
flg = True

while(flg):
    for i in range(len(A_i)):
        if A_i[i] % 2 == 0:
            A_i[i] = A_i[i] / 2
        else:
            flg = False
            break
    if(flg):
        cnt += 1
    else:
        break

print(cnt)