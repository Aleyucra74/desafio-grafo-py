class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range (self.vertices)]

    def adiciona_aresta(self, u, v, peso):
        self.grafo[u-1][v-1] = peso

    def mostra_matriz(self):
        print('Matriz adjacências é: ')

        for i in range(self.vertices):
            print(self.grafo[i])



g = Grafo(4)

g.adiciona_aresta(1, 2,5)
g.adiciona_aresta(3, 4,8)
g.adiciona_aresta(4, 2,6)
g.adiciona_aresta(4, 4,7)

g.mostra_matriz()

