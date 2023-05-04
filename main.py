import math
import numpy as np

#funcao que le o arquivo, calcula a funcao euclidiana e montra matriz de distancia
instances = open("instances.txt")
qtd_instances = int(instances.readline())
cities_coords = {}
graph = np.zeros([qtd_instances, qtd_instances], dtype=float)

for x in range(qtd_instances):
    linha = instances.readline().split()
    a = linha[0]
    b = linha[1]
    cities_coords[x] = a, b

for x in range(qtd_instances):
    px1 = int(cities_coords[x][0])
    py1 = int(cities_coords[x][1])
    
    for y in range(qtd_instances):
        px2 = int(cities_coords[y][0])
        py2 = int(cities_coords[y][1])
        
        if x == y:
            graph[x][y] = 0
        else:
            aux = pow((px2 - px1), 2) + pow((py2 - py1), 2)
            graph[x][y] = math.sqrt(aux)
            
print(graph)
