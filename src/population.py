from individual import Individual
import random

from typing import List, Set, Dict, Tuple, Optional

from utils.ui import Ui
from utils.agent import Agent, Ai
from othello import Othello
from utils.exc import *

POPULATION_SIZE = 8
GENERATION_SIZE = 50


def evolution():
    global POPULATION_SIZE
    global GENERATION_SIZE
    generation = 1

    population = [Individual(Individual.create_gnome())
                  for _ in range(POPULATION_SIZE)]
    print(f'first generation individuals are:')
    for individual in population:
        print(individual.chromosome)

    while True:
        print(generation)
        # print(f'Generation {generation} populations is:')
        # for individual in population:
        #     print(individual.chromosome)

        if generation == GENERATION_SIZE:
            break

        new_generation = []

        for _ in range(POPULATION_SIZE):
            parent1 = random.choice(population)
            parent2 = random.choice(population)

            child = parent1.avg_mate(parent2)
            new_generation.append(child)

        winners = []

        for i, j in zip(population, new_generation):
            winner_num = fight(i.chromosome, j.chromosome)
            winner = i if winner_num == 1 else j
            winners.append(winner)

        population = winners

        generation += 1

    print('best mask: ')
    print(population[0].chromosome)


def fight(mask1, mask2):
    p1: int = -1
    p2: int = 1

    game: Othello = Othello()
    fighter1 = Ai()
    fighter1.positional_mask = mask1
    fighter2 = Ai()
    fighter2.positional_mask = mask2
    players: Tuple[Agent, Agent] = (fighter1, fighter2)

    side: int = p1
    while not game.game_over():
        if game.freeze(side):
            if game.freeze(-1 * side):
                break
            side *= -1
            continue

        curr_player: Agent = players[0 if side == p1 else 1]
        try:
            game.available_moves(side)
            x, y = curr_player.get_move(game, None, side)
            game.play_move(x, y, side)

            # only if everything is ok
            side *= -1
        except EndGameException:
            pass

    winner = game.get_winner()
    return winner


if __name__ == "__main__":
    evolution()
