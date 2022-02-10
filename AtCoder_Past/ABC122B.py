S = input()
char = ["A", "C", "G", "T"]

count = 0
max_count = 0

for s in S:
    if s in char:
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 0

if count > max_count:
    max_count = count

print(max_count)