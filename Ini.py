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


data = {
    1: mapa.escolaB,
    2: mapa.escolaC,
    3: mapa.escolaD,
    4: mapa.escolaE,
    5: mapa.escolaF,
    6: mapa.escolaG,
    7: mapa.escolaH, }

print()
print("1 - Escola Belarmino")
print("2 - Escola Cacilda")
print("3 - Escola Divino")
print("4 - Escola Eufrates")
print("5 - Escola Farrapos")
print("6 - Escola Guilhermino")
print("7 - Escola Hermenegildo")
destino = input("Esolha o numero de Destino: ")
print()
if destino in data:
    Dijkstra.dijkstra_path(listaEscolas, mapa.escolaA, data[int(destino)])
else:
    print("Lamento, opção invalida")
