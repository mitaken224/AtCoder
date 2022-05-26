import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N = int(input())

A = list(map(int, input().split()))
A = set(A)
A = list(A)

print(combinations_count(len(A), 3))