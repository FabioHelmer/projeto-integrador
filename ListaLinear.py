from No import No


class ListaLinear:
    def __init__(self):
        self.prim = No
        self.ult = No
        self.quantNos = 0

    def getPrim(self):
        return self.prim

    def setPrim(self, prim):
        self.prim = prim

    def getUlt(self):
        return self.ult

    def setUlt(self, ult):
        self.ult = ult

    def getQuantNos(self):
        return self.quantNos

    def setQuantNos(self, quantNos):
        self.quantNos = quantNos

    def isVazia(self):
        return self.quantNos == 0

    def add(self, escola):
        no = No(escola)
        if ListaLinear.isVazia(self):
            self.prim = no
        else:
            self.ult.setProx(no)
        self.ult = no
        self.quantNos += 1

    def imprimir(self):
        msg = ""
        atual = self.prim
        while atual != None:
            msg += atual.info.nome
            msg += "-> ("
            for item in atual.info.adjacentes:
                msg += item.escola.nome
                msg += "[{}".format(item.distanciaAdjacencia)
                msg += "]"
            msg += ")"
            print(msg)
            msg = ""
            atual = atual.getProx()
