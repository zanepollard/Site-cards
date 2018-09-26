def importCards():
    cards=".\\cards.txt"
    lines =[]
    with open(cards,'r') as cFile:
        for __ in cFile:
            lines.append(cFile.readline().rstrip('\n').split())
    return lines