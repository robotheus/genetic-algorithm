import sys
import functions as f

def main():
    print("\nGenetic algorithm applied to the traveling salesman problem.\n")

    try:
        graph = f.start(sys.argv[1])
    except:
        return
    
    pop = f.generate_population(graph) 
    popFitness = f.fitness(pop, graph) 
    selectedIndividuos = f.selection(pop, popFitness)
    f.reproduction(selectedIndividuos, int(len(selectedIndividuos)/10))

main()