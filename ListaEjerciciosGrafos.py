#Ejercicio 1
"""
# Grafo representado con listas de adyacencia
class Grafo:                                  
    def __init__(self):                      
        self.grafo = {}                       # Diccionario vacío: {ciudad: [vecinos]} (lista de adyacencia).

    def agregar_ciudad(self, ciudad):         
        if ciudad not in self.grafo:          # Si la ciudad no ha sido agregada aún...
            self.grafo[ciudad] = []           # ...créala con lista de vecinos vacía.

    def agregar_carretera(self, ciudad1, ciudad2):     
        self.grafo[ciudad1].append(ciudad2)            # Conecta ciudad1 -> ciudad2.
        self.grafo[ciudad2].append(ciudad1)            # Conecta ciudad2 -> ciudad1 (grafo NO dirigido).

    def mostrar_grafo(self):                   
        for ciudad, vecinos in self.grafo.items():     # Recorre cada par (ciudad, lista de vecinos).
            print(f"{ciudad} -> {vecinos}")            # Muestra la ciudad y sus conexiones.

    # Algoritmo DFS para encontrar todos los caminos
    def encontrar_caminos(self, inicio, destino, camino=None):  # Busca todos los caminos de inicio a destino.
        if camino is None:                         # Si no te pasaron un camino acumulado (primera llamada)...
            camino = []                            # ...empieza con lista vacía.

        camino = camino + [inicio]                 # Crea una NUEVA lista con el nodo actual al final.
                                                   

        if inicio == destino:                      # Caso base 1: ya llegamos al destino...
            return [camino]                        # ...retorna UNA lista que contiene ESTE camino.

        if inicio not in self.grafo:               # Caso base 2: el inicio no existe en el grafo...
            return []                               # ...no hay caminos.

        caminos = []                                # Acumulará todos los caminos encontrados desde 'inicio'.

        for vecino in self.grafo[inicio]:           # Explora cada vecino de la ciudad actual (DFS).
            if vecino not in camino:                # Evita ciclos: no visites ciudades ya en el camino.
                nuevos_caminos = self.encontrar_caminos(vecino, destino, camino)
                                                   # Llamada recursiva extendiendo el camino hacia 'vecino'.
                for c in nuevos_caminos:            # Por cada camino completo que volvió de la recursión...
                    caminos.append(c)               # ...súmalo a la lista total.
        return caminos                              # Devuelve la lista de TODOS los caminos encontrados.


# Ejemplo de uso
mapa = Grafo()                                     # Crea una instancia del grafo.

# Agregar ciudades
ciudades = ["A", "B", "C", "D", "E"]               # Lista de ciudades que tendrá el mapa.
for ciudad in ciudades:                            # Itera por cada ciudad...
    mapa.agregar_ciudad(ciudad)                    # ...y la agrega (asegura su clave en el diccionario).

# Agregar carreteras
mapa.agregar_carretera("A", "B")                   # Conecta A-B (bidireccional).
mapa.agregar_carretera("A", "C")                   # Conecta A-C.
mapa.agregar_carretera("B", "D")                   # Conecta B-D.
mapa.agregar_carretera("C", "D")                   # Conecta C-D.
mapa.agregar_carretera("D", "E")                   # Conecta D-E.

# Mostrar el grafo
print("Mapa de ciudades y carreteras:")            # Texto informativo.
mapa.mostrar_grafo()                               # Imprime la lista de adyacencia.

# Buscar todos los caminos de A a E
print("\nTodos los caminos posibles de A a E:")    # Texto informativo.
caminos = mapa.encontrar_caminos("A", "E")         # Llama al DFS que devuelve una lista de caminos.
for camino in caminos:                             # Recorre cada camino encontrado...
    print(" -> ".join(camino))                     # ...y lo imprime con flechas entre ciudades.

"""


#Ejercicio 2
"""
from collections import deque   # deque nos da una cola eficiente para BFS

class Grafo:
    def __init__(self):
        self.grafo = {}  # lista de adyacencia: {nodo: [vecinos]}

    def agregar_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = []

    def agregar_arista(self, nodo1, nodo2):
        self.grafo[nodo1].append(nodo2)
        self.grafo[nodo2].append(nodo1)  # grafo no dirigido

    def bfs_camino_corto(self, inicio, destino):
        # Cola para BFS: cada elemento será (nodo_actual, camino_hasta_ahí)
        cola = deque([(inicio, [inicio])])
        visitados = set([inicio])  # conjunto de visitados

        while cola:
            nodo, camino = cola.popleft()  # saca el primero en la cola

            if nodo == destino:            # si llegamos al destino
                return camino              # regresamos el camino completo

            for vecino in self.grafo[nodo]:    # recorremos vecinos
                if vecino not in visitados:    # si no lo hemos visitado aún
                    visitados.add(vecino)      # lo marcamos como visitado
                    cola.append((vecino, camino + [vecino]))  
                    # guardamos el camino extendido

        return None  # si no hay camino, devuelve None


# Ejemplo de uso
mapa = Grafo()
nodos = ["A", "B", "C", "D", "E"]
for n in nodos:
    mapa.agregar_nodo(n)

# Agregar conexiones
mapa.agregar_arista("A", "B")
mapa.agregar_arista("A", "C")
mapa.agregar_arista("B", "D")
mapa.agregar_arista("C", "D")
mapa.agregar_arista("D", "E")

# Buscar camino más corto
inicio, destino = "A", "E"
camino_corto = mapa.bfs_camino_corto(inicio, destino)

print(f"Camino más corto de {inicio} a {destino}: {camino_corto}")
print(f"Longitud mínima: {len(camino_corto)-1} aristas")
"""

#eJERCICIO 3
class RedSocial:
    def __init__(self):
        self.red = {}   # Diccionario: {persona: [lista de amigos]}

    def agregar_persona(self, persona):
        if persona not in self.red:
            self.red[persona] = []

    def agregar_amistad(self, p1, p2):
        # amistad bidireccional
        self.red[p1].append(p2)
        self.red[p2].append(p1)

    def mostrar_red(self):
        for persona, amigos in self.red.items():
            print(f"{persona} -> {amigos}")

    def sugerir_amigos(self, persona):
        if persona not in self.red:
            return []

        amigos_directos = set(self.red[persona])     # tus amigos actuales
        sugerencias = set()

        # recorremos los amigos directos
        for amigo in amigos_directos:
            for amigo_de_amigo in self.red[amigo]:
                # lo sugerimos si no es tú mismo ni tu amigo directo
                if amigo_de_amigo != persona and amigo_de_amigo not in amigos_directos:
                    sugerencias.add(amigo_de_amigo)

        return list(sugerencias)


# Ejemplo de uso
red = RedSocial()

# Agregamos personas
personas = ["Ana", "Beto", "Carla", "Dani", "Elena"]
for p in personas:
    red.agregar_persona(p)

# Creamos amistades
red.agregar_amistad("Ana", "Beto")
red.agregar_amistad("Ana", "Carla")
red.agregar_amistad("Beto", "Dani")
red.agregar_amistad("Carla", "Elena")

print("Red social:")
red.mostrar_red()

# Sugerencias de amigos para Ana
print("\nSugerencias de amigos para Ana:")
print(red.sugerir_amigos("Ana"))
