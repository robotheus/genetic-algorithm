from math import dist

def start():
    instances = open("instances.txt")
    qtd_instances = int(instances.readline())
    cities_coords = {}
    graph = [0] * qtd_instances

    for x in range(qtd_instances):
        linha = instances.readline().split()
        a = linha[0]
        b = linha[1]
        cities_coords[x] = a, b

    for x in range(qtd_instances):
        for y in range(qtd_instances):
            if x == y:
                graph[x][y] = 0
            else:
                graph[x][y] = dist(cities_coords[x], cities_coords[y])

    print(graph)

def main():
    start()