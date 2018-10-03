class card:
    def __init__(self,card,account,description,pin,seq,auth,active):
        self.card = card
        self.account = account
        self.description = description
        self.pin = pin
        self.seq = seq
        self.auth = auth
        self.active = active

    def getActive(self):
        return self.active

    def setActive(self,v):
        self.active = v