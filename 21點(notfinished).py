import random                                                                                # 隨機效果
import time                                                                                  # 計時效果
import operator
suit = ["Spade", "Heart", "Club", "Diamond"]                                                    
face = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]           
facevalue = ["(1, 11)", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"]*4         
cardset = []                                                                                    
point = dict()
sum = 0                                                                                     
Player1 = input("Hello, What's your name?")
time.sleep(1)

def CardSet():
    for w in suit:
        for p in face:
            cardset.append(w+ " "+p)

def PointValue():
    keys = range(52)                                                                          # 用range integer化 -> 用作loop用途
    values = cardset
    for i in keys:
        point[values[i]] = facevalue[i]

def game():                                                                                   #    Game Intro
    print("Alright,", Player1, ", you are going to fight with other players and the banker. Bless you!")
    print("The game will start after 3 seconds")
    time.sleep(3)
    print("Dealer is distributing cards to you")
    time.sleep(2)
    scoring()

def scoring():
    def commoncal():                                                                          #    明牌部分
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
        time.sleep(1)
        print(player, Num, " total point:", sum)

    def calunknown():                                                                        #    暗牌部分
            for player in Playerpoint1:
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
                    print(player, Num, " total point:", sum)
                    continue
                time.sleep(1)
                print(player, "Unknown", "total point: Unknown")

    def decisioncal():                                                                  # hit/stand 部分
        draw = random.choice(list(point))
        time.sleep(1)
        print(player, "has draw", draw)
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

    def exclusion():
        time.sleep(1)
        print(player, "has Stand")
        minus.remove(player)

    def hit1():
        time.sleep(1)
        print(player, "has hit")
        decisioncal()

    def hit2():
        time.sleep(1)
        print(player, "Hit")
        commoncal()

    Playerpoint1 = {Player1: 0, "player 2": 0, "player 3": 0, "player 4": 0, "Banker": 0}       #   計點數
    Playerpoint2 = {Player1: "", "player 2": "", "player 3": "", "player 4": "", "Banker": ""}  #   記牌
    minus = [Player1, "player 2", "player 3", "player 4", "Banker"]

    print("\n\nNew Round\nWith Card Exhibiting")
    for player in Playerpoint1:                                                              
        commoncal()

    print("\n\nWith Card Covered")
    calunknown()                                                                             

    print("\n\n")
    ask = input("stand or hit?").lower()                                # 分歧: 玩家決定stand or hit
    if ask == "stand":                                    # 獨立事件1: 玩家決定stand
        for player in Playerpoint1:
            if player == Player1:                                               # 玩家 stand
                exclusion()
            elif player != Player1 and Playerpoint1[player] > 15:               # 大過15點電腦: stand
                exclusion()
            elif player != Player1 and Playerpoint1[player] < 15:               # 細過15點電腦: hit
                hit1()
                if player != Player1 and Playerpoint1[player] < 15:  
                    hit1()
    elif ask == "hit":                                    # 獨立事件2: 玩家決定hit
        for player in Playerpoint1:
            if player == Player1:
                hit2()
                ask = input("stand or hit?").lower()
                if ask == "stand":
                    exclusion()
                elif ask == "hit":
                    hit2()
                    ask = input("stand or hit?").lower
                    if ask == "stand":
                        print(player, "has Stand")
                    elif ask == "hit":
                        hit2()
            elif player != Player1 and Playerpoint1[player] < 15:
                hit1()
                if player != Player1 and Playerpoint1[player] < 15:
                    hit1()
                elif player != Player1 and Playerpoint1[player] > 15:
                    exclusion()
            elif player != Player1 and Playerpoint1[player] > 15:
                exclusion()

    for player in Playerpoint1:
        if Playerpoint1[player] > 21:
            print(player, "Bust")
        elif Playerpoint1[player] == 21:
            print(player,"has won black Jack")
            break
        elif Playerpoint1[player] == 21:              # 呢度我想整 if 無人=21, then winner = 最接近又細過21既數
            pass
        
    print("\n\nResult:")
    for player in Playerpoint1:
        print(player, "has:", Playerpoint2[player], "             with total point:", Playerpoint1[player])
        
    loop = True
    while loop == True:
        ask = input("would you like to start a New Round?").lower()
        if ask == "yes":
            loop = False
            scoring()
        elif ask == "no":
            quit()
        else:
            print("Sorry, I don't understand. Please try again")
           
CardSet()
PointValue()
game()
