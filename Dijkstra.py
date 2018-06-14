from collections import defaultdict

class Elements:
    def __init__(self):
        self.vertices = set()
        self.aristas = defaultdict(list)
        self.nums = {}
    
    def insertVertice(self,valor):
        self.vertices.add(valor)
    

    def insertArista(self,desde,hasta, valor):
        self.aristas[desde].append(hasta)
        self.aristas[hasta].append(desde)
        self.nums[(desde,hasta)] = valor
        self.nums[(hasta,desde)] = valor

#s es el inicial
def dijkstra(elements, s):
    visitados = {s:0}
    camino = {}

    vertices = set(elements.vertices)

    while(vertices):
        menor = None
        for vertice in vertices:
            if(vertice in visitados):
                if(menor == None):
                    menor = vertice
                elif(visitados[vertice] < visitados[menor]):
                    menor = vertice
        
        if (menor == None):
            break
        
        vertices.remove(menor)
        current = visitados[menor]

        for arista in elements.aristas[menor]:
            peso = current + elements.nums[(menor,arista)]
            if(arista not in visitados or peso < visitados[arista]):
                visitados[arista] = peso
                camino[arista] = menor
        
    return visitados,camino


prueba = Elements()
prueba.insertVertice(1)
prueba.insertVertice(2)
prueba.insertVertice(3)
prueba.insertVertice(4)

prueba.insertArista(1,2,1)
prueba.insertArista(2,3,1)
prueba.insertArista(2,4,2)
prueba.insertArista(3,4,1)
prueba.insertArista(4,1,3)

print dijkstra(prueba,1)





