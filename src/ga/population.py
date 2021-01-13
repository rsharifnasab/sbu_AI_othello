from .individual import Individual
import random

POPULATION_SIZE = 50
GENERATION_SIZE = 100

def evolution():
    global POPULATION_SIZE
    global GENERATION_SIZE
    generation = 1

    population = [Individual(Individual.create_gnome()) for _ in range(POPULATION_SIZE)]

    while True:

        if generation == GENERATION_SIZE:
            break

        new_generation = []

        for _ in range(POPULATION_SIZE):
            parent1 = random.choice(population)
            parent2 = random.choice(population)

            child = parent1.mate(parent2)
            new_generation.append(child)

        survived = []

        for i, j in zip(population, new_generation):
            survivor = fight(i.chromosome, j.chromosome)
            survived.append(survivor)

        population = survived

        generation += 1

    print('best mask: ')
    print(population[0].chromosome)

def fight(mask1, mask2):
    return mask1