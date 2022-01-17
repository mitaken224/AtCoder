N, A, B = map(int, input().split())
ans = 0                     #ans(解答)を0で初期化

for num in range(1, N + 1): #1からNまでの整数をnumに代入
    num_str = str(num)
    sum = 0                 #sum(numの各桁の和)を0で初期化

    for char in num_str:    #numの各桁の和を求めるfor文
        sum += int(char)    #num_strから1文字ずつ取り出し、int型にしてからsumに加算
    
    if A <= sum <= B:       #条件を満たすsumだけansに加算
        ans += num

print(ans)