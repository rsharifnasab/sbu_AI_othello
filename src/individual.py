import random
import numpy as np


class Individual(object):

    def __init__(self, chromosome):
        self.chromosome = chromosome

    @classmethod
    def mutated_genes(self):
        row = np.zeros((1, 8))
        for j in range(8):
            row[0, j] = random.randint(0, 300)
        return row

    @classmethod
    def create_gnome(self):
        mask = np.zeros((8, 8))
        for i in range(8):
            mask[i] = self.mutated_genes()
        return mask

    def row_mate(self, par2):
        child_chromosome = []

        for p1, p2 in zip(self.chromosome, par2.chromosome):

            prob = random.random()

            if prob < 0.45:
                child_chromosome.append(p1)
            elif prob < 0.90:
                child_chromosome.append(p2)
            else:
                child_chromosome.append(self.mutated_genes())

        child_chromosome = np.array(child_chromosome, dtype=object)

        return Individual(child_chromosome)

    def avg_mate(self, par2):
        child_chromosome = []

        for p1, p2 in zip(self.chromosome, par2.chromosome):

            prob = random.random()

            if prob < 0.90:
                child_chromosome.append((p1+p2)/2)
            else:
                child_chromosome.append(self.mutated_genes())

        child_chromosome = np.array(child_chromosome, dtype=object)

        return Individual(child_chromosome)
