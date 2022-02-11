A, B, K = map(int, input().split(" "))
count = 0

for i in range(B, 0, -1):
    if A % i == 0 and B % i == 0:
        count += 1
    if count == K:
        ans = i
        break

print(ans)