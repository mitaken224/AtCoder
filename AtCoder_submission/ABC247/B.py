N = int(input())
name = []
name_set = set()
NG_set = set()

for i in range(N):
    s_i, t_i = input().split()
    name.append([s_i, t_i])

    if s_i in name_set:
        NG_set.add(s_i)

    if t_i in name_set:
        NG_set.add(t_i)

    name_set.add(s_i)
    name_set.add(t_i)        

for ng in NG_set:
    name_set.remove(ng)

flg = True

for n in name:
    if n[0] in name_set:
        continue
    if n[1] in name_set:
        continue
    
    flg = False
    break

if flg:
    print("Yes")
else:
    print("No")