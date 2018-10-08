import card

def importCards():
    cards=".\\cards.txt"
    lines ={}
    with open(cards,'r') as cFile:
        for line in cFile:
            lines[line[0:12].strip()] = card.card(line[0:12].strip(),line[12:36].strip(),line[36:66].strip(),line[66:78].strip(),line[78:102].strip(),line[102:126].strip(),True) 
    return lines
'''
def cardSearch(n, cardList):
    if n in cardList:
        return cardList[n]
'''
def numCheck(n):
    try:
        val = int(n)
    except ValueError:
        return(None, False)
    return (n, True)

def format(x, l):
    for __ in range(l-len(x)):
        x=x+" "
    return x

def cardsOutput(cardList):
    f = open(".\\cards2.txt", 'w+')
    twSpace = "            "
    eSpace = "        "
    for i in cardList:
        if cardList[i].getActive() == True:
            f.write(format(cardList[i].getCard(),12) + format(cardList[i].getAccount(),12) + twSpace + 
                    format(cardList[i].getDescription(),30) + format(cardList[i].getPin(),12) + 
                    format(cardList[i].getSeq(),12) + twSpace + format(cardList[i].getAuth(),12) +
                    twSpace + eSpace + eSpace + "\n")
    f.close()