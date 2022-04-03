x_1, y_1 = map(int, input().split())
x_2, y_2 = map(int, input().split())
x_3, y_3 = map(int, input().split())

if x_1 == x_2:
    x = x_3
elif x_2 == x_3:
    x = x_1
else:
    x = x_2

if y_1 == y_2:
    y = y_3
elif y_2 == y_3:
    y = y_1
else:
    y = y_2

print(x, y)
