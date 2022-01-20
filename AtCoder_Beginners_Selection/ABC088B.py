N = int(input())                        #カードの枚数
card = list(map(int, input().split()))  #カードの数字を配列に格納する

Alice_point = 0 #Aliceの得点を初期化
Bob_point = 0   #Bobの得点を初期化

#cardが無くなるまで
#Alice→Bobの順でカードを取り続け、数字を加算していく
try:
    while(True):
        Alice_point += max(card)    #取ったカードの数字をAlice_pointに加算する
        card.remove(max(card))      #取ったカードをcardから取り除く

        Bob_point += max(card)      #Bobについても上と同様に処理する
        card.remove(max(card))
except:
    print(Alice_point - Bob_point)  #常にAlice_point >= Bob_pointである