a, b, c, d = map(int, input().split(" "))

for Ta in range(a, b + 1):
    Ta_win = True
    for Ao in range(c, d + 1):
        sum = Ta + Ao
        prime = True
        for i in range(2, int(sum ** 0.5) + 1):
            if sum % i == 0:
                prime = False
                break
        if prime:
            Ta_win = False
            break
    if Ta_win:
        break

if Ta_win:
    print("Takahashi")
else:
    print("Aoki")