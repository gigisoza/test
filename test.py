import random

fulldeck = [["2", "spade"], ["3", "spade"], ["4", "spade"], ["5", "spade"], ["6", "spade"], ["7", "spade"], ["8", "spade"], ["9", "spade"], ["10", "spade"], 
            ["j", "spade"], ["q", "spade"], ["k", "spade"], ["a", "spade"],
            ["2", "club"], ["3", "club"], ["4", "club"], ["5", "club"], ["6", "club"], ["7", "club"], ["8", "club"], ["9", "club"], ["10", "club"],
            ["j", "club"], ["q", "club"], ["k", "club"], ["a", "club"],
            ["2", "diamond"], ["3", "diamond"], ["4", "diamond"], ["5", "diamond"], ["6", "diamond"], ["7", "diamond"], ["8", "diamond"], ["9", "diamond"], ["10", "diamond"], 
            ["j", "diamond"], ["q", "diamond"], ["k", "diamond"], ["a", "diamond"], 
            ["2", "heart"], ["3", "heart"], ["4", "heart"], ["5", "heart"], ["6", "heart"], ["7", "heart"], ["8", "heart"], ["9", "heart"], ["10", "heart"], 
            ["j", "heart"], ["q", "heart"], ["k", "heart"], ["a", "heart"]
            ]
board = []
p1 = []
artificial_intelligence = []



def deck():
    random.shuffle(fulldeck)


def p1_turn():
    if len(p1) == 0:
        board.append(fulldeck[0])
        print(f"\nbolo kartia: {fulldeck[0]}")
        fulldeck.pop(0)
        p1_play()
    elif len(p1) > 0:
        print(f"\nairchie karti: {p1}")
        while True:
            cardchoice = int(input("airchie karti indeqsis mixedvit: "))
            board.append(p1[cardchoice])
            p1.pop(cardchoice)
            p1_play()
            break


def artificial_intelligence_turn():
    if len(artificial_intelligence) == 0:
        board.append(fulldeck[0])
        print(f"\nxelovnuri inteleqti chamodis {fulldeck[0]}")
        fulldeck.pop(0)
        artificial_intelligence_play()
    elif len(artificial_intelligence) == 1:
        count = 0      
        board.append(artificial_intelligence[count])
        print(f"\nxelovnuri inteleqti chamodis {artificial_intelligence[0]}")
        artificial_intelligence.pop(count)
        artificial_intelligence_play()
    elif len(artificial_intelligence) > 1:
        count = random.randrange(1, len(artificial_intelligence))
        board.append(artificial_intelligence[count])
        print(f"\nxelovnuri inteleqti chamodis {artificial_intelligence[count]}")
        artificial_intelligence.pop(count)
        artificial_intelligence_play()


def p1_play():
    if  len(board) > 1 and board[-1][1] == board[-2][1]:
        p1.extend(board[:])
        print("\n shegetena")
        board.clear()


def artificial_intelligence_play():
    if  len(board) > 1 and board[-1][1] == board[-2][1]:
        artificial_intelligence.extend(board[:])
        print("\nxelovnur inteleqts sheetena")
        board.clear()


def endgame():
    if len(p1) < len(artificial_intelligence):
        print("gaimarjve!")
    elif len(p1) > len(artificial_intelligence):
        print("waage!")
    else:
        print("fre!")


def deck():
    random.shuffle(fulldeck)


def main():       
    deck()
    while len(fulldeck) > 0:
        p1_turn()
        artificial_intelligence_turn()
    endgame()

main()
