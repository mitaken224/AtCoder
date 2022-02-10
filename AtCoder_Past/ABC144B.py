N = int(input())
flg = False

for i in range(1, 10):
    for j in range(1, 10):
        if N == i * j:
            flg = True
            break
    if flg:
        break

if flg:
    print("Yes")
else:
    print("No")