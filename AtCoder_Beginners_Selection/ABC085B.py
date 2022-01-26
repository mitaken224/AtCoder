N = int(input())

d = []
for i in range(N):
    d_i = int(input())
    d.append(d_i)

count = 1
max_i = max(d)
while(len(d) != 0):
    if max_i > max(d):
        count += 1
    max_i = max(d)
    d.remove(max_i)

print(count)