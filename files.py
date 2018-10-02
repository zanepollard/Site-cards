import card

def importCards():
    cards=".\\cards.txt"
    lines ={}
    with open(cards,'r') as cFile:
        for __ in cFile:
            line = cFile.readline()
            #lines.append(cFile.readline().rstrip('\n').split())
            #lines[line[0:12].strip()] = {'card':line[0:12].strip(),'account' : line[12:36].strip(),'description' : line[36:66].strip(), 'pin' : line[66:78].strip(),'sequence':line[78:102].strip(),'auth':line[102:126].strip()}
            lines[line[0:12].strip()] = card.card(line[0:12].strip(),line[12:36].strip(),line[36:66].strip(),line[66:78].strip(),line[78:102].strip(),line[102:126].strip(),True)

            
    return lines

def numCheck(n):
    try:
        val = int(n)
    except ValueError:
        return(None, False)
    return (n, True)