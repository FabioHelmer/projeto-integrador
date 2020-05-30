# DESENVOLVIDO POR:
# CARLOS BARAQUIEL STEIN DE MEDEIROS
# FABIO HELMER KUHN
# GABRIEL FELIX MENEZES DA SILVA
# JOÃO BATISTA MUYLAERT DE ARAUJO JUNIOR
# WESLEY MARQUES PIZETA
from Escola import Escola
from Adjacente import Adjacente

de = []
escolas = []
para = []
distancia = []

# lendo o arquivo externo para pegar as escolas, e suas distancias
# foi colocado cada coluna do arquivo externo em um vetor
for linha in open("file.csv", encoding="UTF8"):
    de_, para_, distancia_ = linha.split(',')

    if de_ != "De":
        de.append(de_)
    if para_ != "Para":
        para.append(para_)
    if distancia_ != "Distancias\n":
        # retirando o \n
        distancia.append(distancia_[:-1])


# pegando todas as escolas
for i in de:
    if i not in escolas:
        escolas.append(i)
for i in para:
    if i not in escolas:
        escolas.append(i)

# criando as escolas com base nos dados do arquivo externo
escolaA = Escola(escolas[0])
escolaB = Escola(escolas[1])
escolaC = Escola(escolas[2])
escolaD = Escola(escolas[3])
escolaE = Escola(escolas[4])
escolaF = Escola(escolas[5])
escolaG = Escola(escolas[6])
escolaH = Escola(escolas[7])

# limpo o que veio do arquivo e passo armazenar as escolas criadas
escolas.clear()

# criando as adjacencias entre as escolas
# usando a distancia do arquivo externo

escolaA.addAdjacentes(Adjacente(escolaB, distancia[0]),
                      Adjacente(escolaC, distancia[1]), Adjacente(escolaD, distancia[2]))
escolas.append(escolaA)

escolaB.addAdjacentes(Adjacente(escolaC, distancia[3]))
escolas.append(escolaB)

escolaC.addAdjacentes(Adjacente(escolaD, distancia[4]))
escolas.append(escolaC)

escolaD.addAdjacentes(Adjacente(escolaG, distancia[5]), Adjacente(
    escolaE, distancia[6]), Adjacente(escolaF, distancia[7]))
escolas.append(escolaD)

escolaE.addAdjacentes(Adjacente(escolaH, distancia[8]))
escolas.append(escolaE)

escolaF.addAdjacentes(Adjacente(escolaE, distancia[9]))
escolas.append(escolaF)

# se A e ligado em B, logo B e liado em A, é isso que esse algotrimo faz
for escola in escolas:
    for item in escola.getAdjacentes():
        temp = []
        for i in item.escola.getAdjacentes():
            temp.append(i.escola.nome)

        if escola.nome not in temp:
            item.escola.addAdjacente(
                Adjacente(escola, item.distanciaAdjacencia))
