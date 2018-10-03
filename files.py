import card

def importCards():
    cards=".\\cards.txt"
    lines ={}
    with open(cards,'r') as cFile:
        for __ in cFile:
            line = cFile.readline()
            lines[line[0:12].strip()] = card.card(line[0:12].strip(),line[12:36].strip(),line[36:66].strip(),line[66:78].strip(),line[78:102].strip(),line[102:126].strip(),True)

            
    return lines

def numCheck(n):
    try:
        val = int(n)
    except ValueError:
        return(None, False)
    return (n, True)