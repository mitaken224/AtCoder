A = int(input()) # 500円玉の個数
B = int(input()) # 100円玉の個数
C = int(input()) # 50円玉の個数
X = int(input()) # 合計金額

cnt = 0 # 硬貨の選び方の個数

# 3種の硬貨の数でループを回し、それぞれの合計金額を求める
# 合計金額が0になるパターンの数を数える
for a in range(A + 1):
    for b in range(B + 1):
        for c in range(C + 1):
            total = 500 * a + 100 * b + 50 * c
            if total == X:
                cnt += 1
             
print(cnt)