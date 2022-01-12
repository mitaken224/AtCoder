import math

N = int(input())

point_array = []
for i in range(N):
    A = list(map(int, input().split(" ")))
    point_array.append(A)

max_dist = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        dist = math.sqrt((point_array[i][0] - point_array[j][0]) ** 2 + (point_array[i][1] - point_array[j][1]) ** 2)
        if max_dist < dist:
            max_dist = dist

print(max_dist)