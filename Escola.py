class Escola:
    def __init__(self, nome, ):
        self.nome = nome
        self.visitado = False
        self.adjacentes = []

    def addAdjacente(self, escola):
        self.adjacentes.append(escola)

    def addAdjacentes(self, *escolas):
        for escola in escolas:
            self.adjacentes.append(escola)

    def getAdjacentes(self):
        return self.adjacentes
