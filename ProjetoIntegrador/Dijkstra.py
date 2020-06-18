# DESENVOLVIDO POR:
# CARLOS BARAQUIEL STEIN DE MEDEIROS
# FABIO HELMER KUHN
# GABRIEL FELIX MENEZES DA SILVA
# JOÃO BATISTA MUYLAERT DE ARAUJO JUNIOR
# WESLEY MARQUES PIZETA


# retorna a menor distancia de um No origem até um No destino e o caminho até ele
def dijkstra_path(grafo, origem, fim):
    controle = {}
    distanciaAtual = {}
    noAtual = {}
    naoVisitados = []
    atual = origem.nome
    noAtual[atual] = 0
    noGrafo = grafo.getPrim()
    while noGrafo != None:
        # inclui os vertices nos não visitados
        naoVisitados.append(noGrafo.getInfo().nome)
        # inicia os vertices como infinito
        distanciaAtual[noGrafo.getInfo().nome] = float('inf')
        noGrafo = noGrafo.getProx()
    distanciaAtual[atual] = [0, atual]
    naoVisitados.remove(atual)
    noGrafo = grafo.getPrim()
    while naoVisitados:
        for vizinho in noGrafo.getInfo().adjacentes:
            pesoCalc = float(float(vizinho.getDistanciaAdjacencia()
                                   )) + float(noAtual[atual])
            if distanciaAtual[vizinho.escola.nome] == float("inf") or distanciaAtual[vizinho.escola.nome][0] > pesoCalc:
                distanciaAtual[vizinho.escola.nome] = [pesoCalc, atual]
                controle[vizinho.escola.nome] = pesoCalc
                print(controle)

        if controle == {}:
            break
        # seleciona o menor vizinho
        minVizinho = min(controle.items(), key=lambda x: x[1])
        noGrafo = grafo.pesNo(minVizinho[0])
        atual = noGrafo.getInfo().nome
        noAtual[atual] = minVizinho[1]
        naoVisitados.remove(atual)
        del controle[atual]

    print("Custo do caminho é: %s" %
          (distanciaAtual[fim.nome][0]))
    print("O menor caminho é: %s" % printPath(
        distanciaAtual, origem.nome, fim.nome))


def printPath(distancias, inicio, fim):
    if fim != inicio:
        return "%s --> %s" % (printPath(distancias, inicio, distancias[fim][1]), fim)
    else:
        return inicio
