import math
import numpy as np
import sys
import random

def main():
    print("\nGenetic algorithm applied to the traveling salesman problem.\n")

    try:
        graph = start(sys.argv[1]) #le arquivo, calcula dist. euclidiana e retorna matriz de distancias
    except:
        return
    
    try:
        pop = generate_population(graph) #gera população 10 vezes maior que a cidade
    except:
        print("Erro ao gerar a população.")
        return

def start(fileName):
    try:
        instances = open(fileName)
    except:
        print(f'File \'{fileName}\' not found.')
        
    qtd_cities = int(instances.readline())
    cities_coords = {}
    graph = np.zeros([qtd_cities, qtd_cities], dtype = float)

    for x in range(qtd_cities):
        linha = instances.readline().split()
        a = linha[0]
        b = linha[1]
        cities_coords[x] = a, b

    for x in range(qtd_cities):
        px1 = int(cities_coords[x][0])
        py1 = int(cities_coords[x][1])
        
        for y in range(qtd_cities):
            px2 = int(cities_coords[y][0])
            py2 = int(cities_coords[y][1])
            
            if x == y:
                graph[x][y] = 0
            else:
                aux = pow((px2 - px1), 2) + pow((py2 - py1), 2)
                graph[x][y] = math.sqrt(aux)
                
    instances.close()
    return graph

def generate_population(graph):
    cities = []
    sizepop = 10 * len(graph)
    pop = []
    
    for x in range(len(graph)):
        cities.append(x)

    for x in range(sizepop):
        pop.append(random.sample(cities, k = len(graph)))

    return pop

main()

#avaliacao de cada individuo - fitness function
#selecao de alguns individuos para reproducao
#crossover e mutacao
#repetir ate ponto de parada