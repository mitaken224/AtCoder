N, K = map(int, input().split())
A = list(map(int, input().split()))

XY_list = []
for i in range(N):
    XY_list.append(list(map(int, input().split())))

A_list = []
for a in A:
    A_list.append(XY_list[a - 1])

ans = 0
for xy in XY_list:
    min = float('inf')
    for a in A_list:
        dist = ((xy[0] - a[0]) ** 2 + (xy[1] - a[1]) ** 2) ** 0.5
        if dist < min:
            min = dist
    if ans < min:
        ans = min

print(ans)
