# DESENVOLVIDO POR:
# CARLOS BARAQUIEL STEIN DE MEDEIROS
# FABIO HELMER KUHN
# GABRIEL FELIX MENEZES DA SILVA
# JOÃO BATISTA MUYLAERT DE ARAUJO JUNIOR
# WESLEY MARQUES PIZETA
from No import No


class ListaLinear:
    def __init__(self):
        self.prim = None
        self.ult = None
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

    # adicionando uma escola na lista
    def add(self, escola):
        no = No(escola)
        if ListaLinear.isVazia(self):
            self.prim = no
        else:
            self.ult.setProx(no)
        self.ult = no
        self.quantNos += 1

    # pesquisar por uma escola
    def pesNo(self, nome):
        atual = self.prim
        while atual != None:
            if atual.getInfo().nome == nome:
                return atual
            atual = atual.getProx()

    # visualizar os adjacentes de uma escola
    def getAdjascentesCidade(self, escola):
        msg = "({})->".format(escola.nome)
        for i in range(len(escola.getAdjacentes())):
            msg += "[{},".format(escola.adjacentes[i].escola.nome)
            msg += "{}]\n".format(escola.adjacentes[i].distanciaAdjacencia)
        return msg

    # imprimindo o conteudo da lista
    def imprimir(self):
        msg = ""
        atual = self.prim
        while atual != None:
            msg += atual.info.nome
            msg += "->"
            for item in atual.info.adjacentes:
                msg += "({}".format(item.escola.nome)
                msg += "[{}]) ".format(item.distanciaAdjacencia)
            msg += "\n"
            atual = atual.getProx()
        return msg
