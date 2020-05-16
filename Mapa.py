from Escola import Escola
from Adjacente import Adjacente

escolaA = Escola("A")
escolaB = Escola("B")
escolaC = Escola("C")
escolaD = Escola("D")
escolaE = Escola("E")
escolaF = Escola("F")
escolaG = Escola("G")
escolaH = Escola("H")

escolaA.addAdjacentes(Adjacente(escolaB, 8.3),
                      Adjacente(escolaC, 4.4), Adjacente(escolaD, 0.1))

escolaB.addAdjacentes(Adjacente(escolaA, 8.3), Adjacente(escolaC, 8.4))

escolaC.addAdjacentes(Adjacente(escolaB, 8.4), Adjacente(escolaD, 10))

escolaD.addAdjacentes(Adjacente(escolaC, 10), Adjacente(
    escolaG, 5.5), Adjacente(escolaE, 0.8), Adjacente(escolaF, 8))

escolaE.addAdjacentes(Adjacente(escolaD, 0.8), Adjacente(escolaH, 7.2))

escolaF.addAdjacentes(Adjacente(escolaD, 8), Adjacente(escolaE, 6.4))

escolaG.addAdjacentes(Adjacente(escolaD, 5.5))

escolaH.addAdjacentes(Adjacente(escolaE, 7.2))


def getAdjascentesCidade(escola):
    for i in range(len(escola.adjacentes)):
        print(escola.adjacentes[i].escola.nome)
        print(escola.adjacentes[i].distanciaAdjacencia)

