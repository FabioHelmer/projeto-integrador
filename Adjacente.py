# DESENVOLVIDO POR:
# CARLOS BARAQUIEL STEIN DE MEDEIROS
# FABIO HELMER KUHN
# GABRIEL FELIX MENEZES DA SILVA
# JOÃO BATISTA MUYLAERT DE ARAUJO JUNIOR
# WESLEY MARQUES PIZETA


class Adjacente:
    def __init__(self, escola, distancia):
        self.escola = escola
        self.distanciaAdjacencia = distancia

    def setDistanciaAdjacencia(self, distancia):
        self.distanciaAdjacencia = distancia

    def getDistanciaAdjacencia(self):
        return self.distanciaAdjacencia
