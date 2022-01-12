#### D ####
N, K = map(int,input().split(" "))
P = list(map(int, input().split(" ")))

sorted_P = sorted(P[:K])

print(sorted_P[0])

for i in range(K, N):
    flg = True
    
    for j in range(len(sorted_P)):
        if P[i] < sorted_P[j]:
            sorted_P.insert(j, P[i])
            flg = False
            break
            
    if flg:
        sorted_P.append(P[i])

    print(sorted_P[-K])


#### D ####
from bisect import insort

N, K = map(int,input().split(" "))
P = list(map(int, input().split(" ")))

sorted_P = sorted(P[:K])

print(sorted_P[0])

for i in range(K, N):
    insort(sorted_P, P[i])

    print(sorted_P[-K])
