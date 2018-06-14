from collections import defaultdict

class Element:
    def __init__(self,cant):
        self.V = cant
        self.elements = []
    
    def insertar(self,desde,hasta,valor):
        self.elements.append([desde,hasta,valor])
    

    def imprimirArr(self,canti):
        for a in range(self.V):
            print(a,canti[a])
    

    def bellman_ford(self,s):
        camino = [float("Inf")] * self.V
        camino[s] = 0

        for a in range(self.V-1):
            for desde,hasta,valor in self.elements:
                if(camino[desde] != float("Inf") and camino[desde] + valor < camino[hasta]):
                    camino[hasta] = camino[desde] + valor

        for desde,hasta,valor in self.elements:
                if(camino[desde] != float("Inf") and camino[desde] + valor < camino[hasta]):
                    return
        
        self.imprimirArr(camino)


prueba = Element(4)

prueba.insertar(0,1,1)
prueba.insertar(0,2,-1)
prueba.insertar(0,3,-3)
prueba.insertar(1,3,2)
prueba.insertar(2,3,2)
prueba.insertar(3,1,4)
prueba.insertar(3,0,3)

prueba.bellman_ford(0)



