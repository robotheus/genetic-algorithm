import math
import numpy as np
import sys

def main():
    print("\nGenetic algorithm applied to the traveling salesman problem.\n")
    
    try:
        start(sys.argv[1]) #le o arquivo, calcula a distancia euclidiana e retorna a matriz de distancias/adjacencia
    except:
        return

def start(fileName):
    try:
        instances = open(fileName)
    except:
        print(f'File \'{fileName}\' not found.')
        
    qtd_instances = int(instances.readline())
    cities_coords = {}
    graph = np.zeros([qtd_instances, qtd_instances], dtype = float)

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
                
    instances.close()
    print(graph)
    return graph

main()

#inicializacao da populacao
#avaliacao de cada individuo - fitness function
#selecao de alguns individuos para reproducao
#crossover e mutacao
#