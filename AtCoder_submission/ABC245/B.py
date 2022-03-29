N = int(input())
A = list(map(int, input().split()))

list = [False] * 2001

for A_i in A:
    list[A_i] = True

for i in range(2001):
    if list[i] == False:
        print(i)
        break