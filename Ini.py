from ListaLinear import ListaLinear
import Mapa as map
import Dijkstra

listaEscolas = ListaLinear()
listaEscolas.add(map.escolaA)
listaEscolas.add(map.escolaB)
listaEscolas.add(map.escolaC)
listaEscolas.add(map.escolaD)
listaEscolas.add(map.escolaE)
listaEscolas.add(map.escolaF)
listaEscolas.add(map.escolaG)
listaEscolas.add(map.escolaH)

Dijkstra.dijkstra_path(listaEscolas, map.escolaA, map.escolaC)
