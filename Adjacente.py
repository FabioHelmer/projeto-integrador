# DESENVOLVIDO POR:
# CARLOS BARAQUIEL STEIN DE MEDEIROS
# FABIO HELMER KUHN
# GABRIEL FELIX MENEZES DA SILVA
# JOÃO BATISTA MUYLAERT DE ARAUJO JUNIOR
# WESLEY MARQUES PIZETA


class Adjacente:
    def __init__(self, escola, distancia):
        # objeto criado para guardar a escola que é adjascente
        # e guardar a distancia
        self.escola = escola
        self.distanciaAdjacencia = distancia

    def setDistanciaAdjacencia(self, distancia):
        self.distanciaAdjacencia = float(distancia)

    def getDistanciaAdjacencia(self):
        return self.distanciaAdjacencia

    def getEscola(self):
        return self.escola
