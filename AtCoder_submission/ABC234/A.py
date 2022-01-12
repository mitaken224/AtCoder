t = int(input())

def f_x(x):
    y = x ** 2 + x * 2 + 3
    return y

ans = f_x(f_x(f_x(t) + t) + f_x(f_x(t)))
print(ans)