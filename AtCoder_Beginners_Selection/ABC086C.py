N = int(input())

goal = []
for i in range(N):
    goal.append(list(map(int, input().split(" "))))

t = 0
x = 0
y = 0

flg = True
for i in range(N):
    t_next = goal[i][0]
    x_next = goal[i][1]
    y_next = goal[i][2]

    t_gap = t_next - t
    x_gap = x_next - x
    y_gap = y_next - y

    if abs(x_gap) + abs(y_gap) <= t_gap:
        if (x_gap + y_gap) % 2 == t_gap % 2:
            t = t_next
            x = x_next
            y = y_next
            continue

    flg = False
    break

if flg:
    print("Yes")
else:
    print("No")