from collections import deque

N = int(input())
S = input()
W = list(map(int, input().split()))

zip_list = zip(W, S)
zip_list = sorted(zip_list)
W, S = zip(*zip_list)

f_x = S.count("0")
max = f_x

d_S = deque(S)
d_W = deque(W)

for i in range(len(d_S)):
    pop_S = d_S.pop()
    pop_W = d_W.pop()

    if pop_S == "1":
        f_x += 1
    elif pop_S == "0":
        f_x -= 1
    
    if len(d_W) == 0 or pop_W != d_W[-1]:
        if f_x > max:
            max = f_x
    
print(max)