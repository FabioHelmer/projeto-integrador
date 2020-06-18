# DESENVOLVIDO POR:
# CARLOS BARAQUIEL STEIN DE MEDEIROS
# FABIO HELMER KUHN
# GABRIEL FELIX MENEZES DA SILVA
# JOÃO BATISTA MUYLAERT DE ARAUJO JUNIOR
# WESLEY MARQUES PIZETA

from ListaLinear import ListaLinear
import Mapa as mapa
import Dijkstra

listaEscolas = ListaLinear()
listaEscolas.add(mapa.escolaA)
listaEscolas.add(mapa.escolaB)
listaEscolas.add(mapa.escolaC)
listaEscolas.add(mapa.escolaD)
listaEscolas.add(mapa.escolaE)
listaEscolas.add(mapa.escolaF)
listaEscolas.add(mapa.escolaG)
listaEscolas.add(mapa.escolaH)

Dijkstra.dijkstra_path(listaEscolas, mapa.escolaA, mapa.escolaH)
