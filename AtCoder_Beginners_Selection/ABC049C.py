S = input()
S = S[::-1] # 入力された文字列Sを逆順にする

divide = ["dream", "dreamer", "erase", "eraser"]
for i in range(len(divide)):
    divide[i] = divide[i][::-1] # Tに追加できる4つの文字列も逆順にする

i = 0   # 現在Sの何文字目をサーチしているか
ans = True  # S=Tにできたかどうか

while i < len(S):   # Sの最後の文字までサーチができたら終了
    flg = False     # Tに適切な文字列を追加できたかどうか

    for d in divide:    # 4つの文字列から1個ずつ試してみる
        if S[i : i + len(d)] == d:  #適切な文字列が見つかったとき
            flg = True
            i += len(d)
            break

    if flg == False:    #適切な文字列が見つからなかったとき
        ans = False
        break

if ans:
    print("YES")
else:
    print("NO")