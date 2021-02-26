import random  # 隨機效果
import time  # 計時效果

suit = ["Spade", "Heart", "Club", "Diamond"]
face = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
facevalue = ["(1, 11)", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"] * 4
cardset = []
point = dict()
sum = 0
Player1 = input("Hello, What's your name?")
time.sleep(1)

def CardSet():
    for w in suit:
        for p in face:
            cardset.append(w + " " + p)

def PointValue():
    keys = range(52)                                                # 用range integer化 -> 用作loop用途
    values = cardset
    for i in keys:
        point[values[i]] = facevalue[i]

def game():  # Game Intro
    print("Alright,", Player1, ", you are going to fight with other players and the banker. Bless you!")
    print("The game will start after 3 seconds")
    time.sleep(3)
    print("Dealer is distributing cards")
    time.sleep(1)
    scoring()

def scoring():
    def commoncal():                                   # 亮牌部分
        draw = random.choice(list(point))              # 隨機派牌(但呢個方式會有重複, 可能要用pop/remove 功能/其他random方式)
        Cpt = point.get(draw)
        Num = Playerpoint2.get(player) + " " + draw
        Playerpoint2[player] = Num
        if Cpt == "(1, 11)":
            if Playerpoint1[player] > 10:               #用total點數決定ace既點數
                pt = 1
            else:
                pt = 11
        else:
            pt = int(Cpt)
        ptt = pt
        sum = Playerpoint1.get(player) + ptt
        Playerpoint1[player] = sum
        time.sleep(1)
        if a == 5:
            delay()
            print(player, Num, " total point:", sum)
        elif zzz == 100:                                                # 玩家hit 牌
            if player == Player1:
                print(player, "decides to Hit, and receives", draw, "total:", sum)
            elif player != Player1:                                     # cpu玩家hit 牌
                delay()
                print(player, "decides to Hit, and receives", draw)

    def calunknown():                                          # 暗牌部分
        for player in Playerpoint1:
            if player != Player1:
                print(player,":", Playerpoint2[player], "+ ?, total point:", Playerpoint1[player], "+ ?")
            draw = random.choice(list(point))                        
            Cpt = point.get(draw)
            Num = Playerpoint2.get(player) + " " + draw
            Playerpoint2[player] = Num
            if Cpt == "(1, 11)":
                if Playerpoint1[player] > 10:
                    pt = 1
                else:
                    pt = 11
            else:
                pt = int(Cpt)
            ptt = pt
            sum = Playerpoint1.get(player) + ptt
            Playerpoint1[player] = sum
            if player == Player1:
                time.sleep(1)
                print(player,":", Num, " total point:", sum)
                continue
            time.sleep(1)

    def hit():
        time.sleep(1)
        delay()
        commoncal()

    def delay():                                                                  #調慢速度
        if player == Player1:
            print("waiting ..............")
            time.sleep(2)

    Playerpoint1 = {Player1: 0, "player 2": 0, "player 3": 0, "player 4": 0, "Banker": 0}  # 計點數
    Playerpoint2 = {Player1: "", "player 2": "", "player 3": "", "player 4": "", "Banker": ""}  # 記牌
    minus = [Player1, "player 2", "player 3", "player 4", "Banker"]  # stop loop, 避免重覆出現meessage: (a stand.. a stand. a stand)

    print("\n\nNew Round\nWith Card Exhibiting")
    for player in Playerpoint1:
        a = 5                                       # show point
        commoncal()
        a = 0

    print("\n\nWith Card Covered")
    calunknown()

    print("\n\n")
    HitAndSt = True
    while HitAndSt == True:
        ask = input("stand or hit          ").lower()
        if ask == "hit":              # 獨立事件1: 玩家決定hit  (目前夠用, 但可以改更好)
            zzz = 100                                # enable hit 牌情況出現                      
            for player in minus:
                if player == Player1:
                    hit()                                        # 玩家hit 牌
                elif player != Player1 and Playerpoint1[player] < 15:
                    hit()                                         # 玩家hit 牌
                elif player != Player1 and Playerpoint1[player] >= 15:
                    print(player, "decides to Stand")
                    minus.remove(player)
                    delay()

        elif ask == "stand":
            zzz = 100
            HitAndSt = False
            fff = 3
            while  fff > 0:                         
                for player in minus:                  
                    if len(minus) <2: fff = fff -999   #如果全部都stand就停                       
                    elif player == Player1:
                        print(player, "decides to Stand")
                        delay()
                    elif player != Player1:
                        if Playerpoint1[player] >= 15:
                            print(player, "decides to Stand")
                            minus.remove(player)
                            delay()
                        elif Playerpoint1[player] < 15:
                            hit()
                            
        elif ask != "hit" and ask !="stand":
            print("Sorry, I don't understand.")
    zzz = 0
    for player in Playerpoint1:
        if Playerpoint1[player] > 21:
            print(player, "Bust")
        elif Playerpoint1[player] == 21:
            print(player, "has won black Jack")
            break
        elif Playerpoint1[player] == 21:  # 未整好 :呢度我想整 if 無人=21, then winner = 最接近又細過21既數,but 唔識整 
            pass

    print("\n\nResult:")
    for player in Playerpoint1:
        print(player, "has:", Playerpoint2[player], "             with total point:", Playerpoint1[player])
        time.sleep(0.5)

    print("\n\n")
    loop = True
    while loop == True:
        ask = input("would you like to start a New Round?").lower()
        if ask == "yes":
            loop = False
            scoring()
        elif ask == "no":
            print("See You")
            break
        else:
            print("Sorry, I don't understand. Please try again")

CardSet()
PointValue()
game()
