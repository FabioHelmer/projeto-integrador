class No:
    def __init__(self, escola):
        self.info = escola
        self.prox = None

    def setProx(self, prox):
        self.prox = prox

    def getProx(self):
        return self.prox

    def setInfo(self, info):
        self.info = info

    def getInfo(self):
        return self.info
