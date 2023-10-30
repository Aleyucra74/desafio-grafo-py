class Grafo:

    def __init__(self,vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range (self.vertices)]

    def adiciona_aresta(self, u, v):
        self.grafo[u-1][v-1] = 1

    def mostra_matriz(self):
        print('Matriz adjacências é: ')

        for i in range(self.vertices):
            print(self.grafo[i])



g = Grafo(4)

g.adiciona_aresta(1, 2)
g.adiciona_aresta(1, 3)
g.adiciona_aresta(4, 2)
g.adiciona_aresta(4, 1)

g.mostra_matriz()


