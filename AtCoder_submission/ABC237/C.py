def judge(str):
    N = len(str)
    flg = True
    
    for i in range(int(N/2)):
        if str[i] != str[N-1-i]:
            flg = False
            break

    return flg

S = input()

cnt = 1
while(True):
    flg = judge(S)
    if flg:
        print("Yes")
        break
    else:
        if S[-cnt] == "a":
            S = "a" + S
            cnt += 1
        else:
            print("No")
            break