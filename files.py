import card
import csv

def importCards(pathname):
    lines ={}
    with open(pathname,'r') as cFile:
        for line in cFile:
            lines[line[0:12].strip()] = card.card(line[0:12].strip(),line[12:36].strip(),line[36:66].strip(),line[66:78].strip(),line[78:102].strip(),line[102:126].strip(),True) 
    return lines

def importData(pathname):
    firstline = True
    lines={}
    active = False
    with open(pathname, newline='') as csvfile:
        csvreader = csv.reader(csvfile,quotechar='\"')
        for row in csvreader:
            active = False
            if firstline:
                firstline=False
                continue
            if row[6] =='True':
                active = True
            lines[row[0]] = card.card(row[0],row[1],row[2],row[3],row[4],row[5],active)
    return lines        

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

def cardsOutput(cardList,pathname):
    f = open(pathname, 'w+')
    twSpace = "            "
    eSpace = "        "
    for i in cardList:
        if cardList[i].getActive() == True:
            f.write(format(cardList[i].getCard(),12) + format(cardList[i].getAccount(),12) + twSpace + 
                    format(cardList[i].getDescription(),30) + format(cardList[i].getPin(),12) + 
                    format(cardList[i].getSeq(),12) + twSpace + format(cardList[i].getAuth(),12) +
                    twSpace + eSpace + eSpace + "\n")
    f.close()

def dataExport(cardList,pathname):
    with open(pathname, 'w', newline='') as csvfile:
        cardwriter = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_ALL)
        cardwriter.writerow(('card','account','description','pin','seq','auth','active'))
        for i in cardList:
            cardwriter.writerow((cardList[i].getCard(),cardList[i].getAccount(),cardList[i].getDescription(),cardList[i].getPin(),cardList[i].getSeq(),cardList[i].getAuth(),cardList[i].getActive()))