from tkinter.tix import InputOnly


N = int(input())
S = []
time_list = []

for i in range(N):
    S.append(input())

for j in range(10):
    l = []
    for i in range(N):
        sec = S[i].find(str(j))
        l.append(sec)
    time_list.append(l)

min = 10000
for j in range(10):
    time_list[j].sort()
    l = time_list[j]
    cnt = 0
    for k in range(len(l) - 1):
        if l[k] == l[k + 1]:
            cnt += 1
            flg = True
        elif flg and l[k] != l[k + 1]:
            l[k] += cnt * 10
    if flg:
        l[-1] += cnt * 10
    
    if min > max(l):
        min = max(l)

print(min)