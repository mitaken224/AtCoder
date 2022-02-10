N = int(input())

if N < 10:
    ans = N
elif N < 100:
    ans = 9
elif N < 1000:
    ans = N - 90    # 9 + (N - 99)
elif N < 10000:
    ans = 909
elif N < 100000:
    ans = N - 9090  # 909 + (N - 9999)
else:
    ans = 90909
    
print(ans)