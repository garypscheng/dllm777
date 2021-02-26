# 導入模組
import random                                                                                # 隨機效果
import time                                                                                  # 計時效果
import operator

#前設部分
c = ["Spade", "Heart", "Club", "Diamond"]                                                    # 花色
v = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]           # 牌面
n = ["(1, 11)", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"]*4            # 面值 (確保v, n 既list items 係一樣(之後用黎直接整合))
card = []                                                                                    # 即將整既牌set
point = dict()
sum = 0                                                                                      # 計total點數
name = input("Hello, What's your name?")
time.sleep(1)

# Function Definitions 部分:                                             
def CardSet():                                                                               # 生成一副牌                          
    for w in c:
        for p in v:
            card.append(w+ " "+p)

def PointValue():
    keys = range(52)                                                                         # 用range integer化 -> 用作loop用途
    values = card
    for i in keys:
        point[values[i]] = n[i]

def game():                                                                                  # 開場白
    print("Alright,", name, ", you are going to fight with other players and the banker. Bless you!")
    print("The game will start after 3 seconds")
    time.sleep(3)
    print("Dealer is distributing cards to you")
    time.sleep(2)
    scoring()

def scoring():
    def commoncal():                                                                          # 明牌部分calculation
        draw = random.choice(list(point))                                                     # 隨機抽牌
        Cpt = point.get(draw)                                                                 # 利用dict功能show key所代表的數值
        Num = Playerpoint2.get(player) + " " + draw                                           # 記起抽到咩牌
        Playerpoint2[player] = Num
        if Cpt == "(1, 11)":                                                                  # 計分部分
            if Playerpoint1[player] > 10:                                                     # Ace 點數根據玩家總得分而決定為1/11
                pt = 1
            else:
                pt = 11
        else:
            pt = int(Cpt)                                                                     # 其他牌直接轉換其點數
        ptt = pt
        sum = Playerpoint1.get(player) + ptt
        Playerpoint1[player] = sum
        print(player, Num, " total point:", sum)

    def calunknown():                                                                        #    暗牌部分calculation
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
                if player == name:                                                            #    增加了除自己玩家外其他總分為未知數 (暗牌)
                    print(player, Num, " total point:", sum)
                    continue
                print(player, "Unknown", "total point: Unknown")

    def decisioncal():                                                                  # 用於hit/stand 部分
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
        Playerpoint1[player] = sum                                                       # 與commoncal()相比,佢缺少print總分既部分

    def exclusion():                                                                     # 當玩家決定stand時, 為避免佢地會一直重複講xxx Stand, 而決定將其由list剔出
        print(player, "has Stand")
        minus.remove(player)

    def hit1():                                                                          # hit 計算方式
        print(player, "has hit")
        decisioncal()

    def hit2():
        print(player, "has hit")
        commoncal()
   
    Playerpoint1 = {name: 0, "player 1": 0, "player 2": 0, "player 3": 0, "Banker": 0}       #   for 計分用
    Playerpoint2 = {name: "", "player 1": "", "player 2": "", "player 3": "", "Banker": ""}  #   for 計牌用
    minus = [name, "player 1", "player 2", "player 3", "Banker"]                             #   for 剔除用: 費時不停重覆player 1 has Stand, player 1 has Stand, player 1 has Stand
        
    print("\n\nNew Round\nWith Card Exhibiting")
    for player in Playerpoint1:                                                              #    明牌
        commoncal()

    print("\n\nWith Card Covered")
    calunknown()                                                                             #    暗牌

    print("\n\n")
    ask = input("stand or hit?")                                 # 分歧: 玩家決定stand or hit
    askk = ask.lower()
    if askk == "stand":                                          # 獨立事件1: 玩家決定stand
        for player in Playerpoint1:
            if player == name:                                               # 玩家 stand
                exclusion()
            elif player != name and Playerpoint1[player] > 15:               # 大過15點的電腦玩家: stand
                exclusion()
            elif player != name and Playerpoint1[player] < 15:               # 細過15點的電腦玩家: hit
                hit1()
                if player != name and Playerpoint1[player] < 15:  # 細過15點的電腦玩家: hit
                    hit1()
    elif askk == "hit":                                           # 獨立事件2: 玩家決定hit
        for player in Playerpoint1:
            if player == name:
                hit2()
                ask = input("stand or hit?")                      # 分歧: 玩家決定stand or hit
                askk = ask.lower()
                if askk == "stand":
                    exclusion()
                elif askk == "hit":
                    hit2()
                    ask = input("stand or hit?")                  # 分歧: 玩家決定stand or hit
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
    print(Playerpoint1)
    print(Playerpoint2)


# Call Functions 
CardSet()
PointValue()
game()
