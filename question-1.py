import random

vertices = ['P1','P2','P5','P6']

class Capella:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*len(self.vertices) for i in enumerate(self.vertices)]
#        print(self.grafo[0][1])

    def add_aresta(self, u, v,weight):
        self.grafo[u][v] = weight

    def show_capella(self):
        for index,i in enumerate(self.vertices):
            print(i,':', self.grafo[index])
            
    def win_lose(self):
        len_dimension=0
        sum_values_weight=0
        points=[]
        for i in self.grafo:
            len_dimension+=len(i)
        
        for j in range(len_dimension):
            n1 = random.randint(0,3)
            n2 = random.randint(0,3)
            sum_values_weight += self.grafo[n1][n2]
            points.append(sum_values_weight)

        print('pontos max: ',max(points))
        print('pontos min: ',min(points))

capella = Capella(vertices)
print('adding vertices:')

capella.add_aresta(0,1,11)
capella.add_aresta(0,2,5)
capella.add_aresta(0,3,0)
capella.add_aresta(1,0,11)
capella.add_aresta(1,2,4)
capella.add_aresta(2,1,4)
capella.add_aresta(2,0,5)
capella.add_aresta(2,3,6)
capella.add_aresta(3,0,0)
capella.add_aresta(3,2,6)

capella.show_capella()
#capella.win_lose()

