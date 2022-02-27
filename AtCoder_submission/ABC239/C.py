a, b, c, d = map(int, input().split(" "))
flg = False

for x in range(a - 2, a + 3):
    for y in range(b - 2, b + 3):
        if (x - a) ** 2 + (y - b) ** 2 == 5 and (x - c) ** 2 + (y - d) ** 2 == 5:
            flg = True
            break

if flg:
    print("Yes")
else:
    print("No")