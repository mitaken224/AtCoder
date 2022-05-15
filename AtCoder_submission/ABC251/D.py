W = int(input())

for i in range(3, 301):
    C = i + (i * (i - 1) / 2) + (i * (i - 1) * (i - 2)/ 6)
    if W < C:
        print(i)
        break