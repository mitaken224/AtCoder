R, C = map(int, input().split())

l = []
for i in range(2):
    l.append(list(map(int, input().split())))

print(l[R - 1][C - 1])
