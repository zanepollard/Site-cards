class card:
    def __init__(self,card,account,description,pin,seq,auth,active):
        self.card = card
        self.account = account
        self.description = description
        self.pin = pin
        self.seq = seq
        self.auth = auth
        self.active = active

    def setActive(self,v):
        self.active = v

    def setAccount(self,v):
        self.account = v
    
    def setDescription(self,v):
        self.description = v
    
    def setPin(self,v):
        self.pin = v
    
    def setSeq(self,v):
        self.seq = v

    def setAuth(self,v):
        self.auth = v

    def getCard(self):
        return self.card

    def getAccount(self):
        return self.account

    def getDescription(self):
        return self.description

    def getPin(self):
        return self.pin

    def getSeq(self):
        return self.seq

    def getAuth(self):
        return self.auth
    
    def getActive(self):
        return self.active

    