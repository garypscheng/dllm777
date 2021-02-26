import random                                                                                # 隨機效果
import time                                                                                  # 計時效果
import operator
c = ["Spade", "Heart", "Club", "Diamond"]                                                    # 花色
v = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]           # 牌面
n = ["(1, 11)", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"]*4            # 面值
card = []                                                                                    # 即將整既牌set
point = dict()
sum = 0                                                                                      # 計total點數
name = input("Hello, What's your name?")
time.sleep(1)

def CardSet():
    for w in c:
        for p in v:
            card.append(w+ " "+p)

def PointValue():
    keys = range(52)                                                                          # 用range integer化 -> 用作loop用途
    values = card
    for i in keys:
        point[values[i]] = n[i]

def game():                                                                                   #    Game Intro
    print("Alright,", name, ", you are going to fight with other players and the banker. Bless you!")
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
                if player == name:
                    print(player, Num, " total point:", sum)
                    continue
                print(player, "Unknown", "total point: Unknown")
            print(Playerpoint1)

    def decisioncal():                                                                  # hit/stand 部分
        draw = random.choice(list(point))
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
        print(player, "has Stand")
        minus.remove(player)

    def hit1():
        print(player, "has hit")
        decisioncal()

    def hit2():
        print(player, "Hit")
        commoncal()


    a = 5
    Playerpoint1 = {name: 0, "player 1": 0, "player 2": 0, "player 3": 0, "Banker": 0}       #   for 計分用
    Playerpoint2 = {name: "", "player 1": "", "player 2": "", "player 3": "", "Banker": ""}  #   for 計牌用
    minus = [name, "player 1", "player 2", "player 3", "Banker"]

    print("\n\nNew Round\nWith Card Exhibiting")
    for player in Playerpoint1:                                                              #    明牌
        commoncal()

    print("\n\nWith Card Covered")
    calunknown()                                                                             #    暗牌

    print("\n\n")
# 1: 玩家決定stand or hit
     #a) stand: 玩家不抽, 而cpu判定stand or hit  -->single loop
     #b) hit: 玩家抽和點數<15的玩家一起抽 -->再問(stand or hit) --> hit: 玩家抽和點數<15的玩家一起抽 --->loop: 直到玩家答stand (while)

# 2: CPU決定stand or hit    --> 用while 或者 if xx= True
     # ai) 當cpu點數>15:決定stand: 其餘<15的決定抽
     # aii) 當cpu點數<15: 決定hit --> looping aii) until false -->back to ai)
# 3: 判定階段:
     # 全部玩家都stand --> if statement
     # i) if 點數=21 --> direct winner
     # ii) if 點數>21 --> 該名玩家直接輸, 其餘的最接近而小於21點的為勝
     # iii) if 點數<21 :最接近而小於21點的玩家為勝

    
    ask = input("stand or hit?")                                 # 分歧: 玩家決定stand or hit
    askk = ask.lower()
    if askk == "stand":                                    # 獨立事件1: 玩家決定stand
        for player in Playerpoint1:
            if player == name:                                               # 玩家 stand
                exclusion()
            elif player != name and Playerpoint1[player] > 15:               # 大過15點的電腦玩家: stand
                exclusion()
            elif player != name and Playerpoint1[player] < 15:               # 細過15點的電腦玩家: hit
                hit1()
                if player != name and Playerpoint1[player] < 15:  # 細過15點的電腦玩家: hit
                    hit1()
    elif askk == "hit":                                    # 獨立事件2: 玩家決定hit
        for player in Playerpoint1:
            if player == name:
                hit2()
                ask = input("stand or hit?")  # 分歧: 玩家決定stand or hit
                askk = ask.lower()
                if askk == "stand":
                    exclusion()
                elif askk == "hit":
                    hit2()
                    ask = input("stand or hit?")  # 分歧: 玩家決定stand or hit
                    askk = ask.lower()
                    if askk == "stand":
                        print(player, "has Stand")
                    elif askk == "hit":
                        hit2()
            elif player != name and Playerpoint1[player] < 15:
                hit1()
                if player != name and Playerpoint1[player] < 15:
                    hit1()
                elif player != name and Playerpoint1[player] > 15:
                    exclusion()
            elif player != name and Playerpoint1[player] > 15:
                exclusion()

    for player in Playerpoint1:
        if Playerpoint1[player] > 21:
            print(player, "Bust")
        elif Playerpoint1[player] == 21:
            print(player,"has won black Jack")
            break
        elif Playerpoint1[player] == 21:              # 呢度我想整 if 無人=21, then winner = 最接近又細過21既數
            pass
    
    for player in Playerpoint1:
        print(player, "has:", Playerpoint2[player], "             with total point:", Playerpoint1[player])



CardSet()
PointValue()
game()
