from ListaLinear import ListaLinear
import Mapa as map
import Dijkstra

lista = ListaLinear()
lista.add(map.escolaA)
lista.add(map.escolaB)
lista.add(map.escolaC)
lista.add(map.escolaD)
lista.add(map.escolaE)
lista.add(map.escolaF)
lista.add(map.escolaG)
lista.add(map.escolaH)

print(lista.imprimir())
Dijkstra.dijkstra_path(lista, map.escolaA, map.escolaH)
