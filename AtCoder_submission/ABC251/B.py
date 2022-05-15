import itertools

N, W = map(int, input().split())
A = list(map(int, input().split()))

S = set()

for a in A:
    if a <= W:
        S.add(a)

for a in itertools.combinations(A, 2):
    if sum(a) <= W:
        S.add(sum(a))

for a in itertools.combinations(A, 3):
    if sum(a) <= W:
        S.add(sum(a))

print(len(S))