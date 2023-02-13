import numpy as np
import time
from tqdm import tqdm
import random
import os
import time
import pickle

test_path = './testcase for Truong'


def load_data(path='.'):
    with open(path, "r") as file:
        # read the file line by line
        lines = file.readlines()
        # convert each line to integer and append to the list
        conditions = [[int(i) for i in line.strip().split(' ')] for line in lines if len(line.strip()) > 0]

    N = conditions[0][0]
    A = conditions[0][1]
    C = conditions[0][2]
    c = conditions[1]
    a = conditions[2]
    f = conditions[3]
    m = conditions[4]
    return N, A, C, c, a, f, m


def check_constrain(inputs):
    cost = np.sum(inputs * (inputs >= m) * c)
    area = np.sum((inputs * (inputs >= m)) * a)

    if cost > C or area > A:
        return False
    return True


def generate_population(pop_size, chrom_len):
    # generate a population of pop_size individuals, each with a chromosome of length chrom_len
    x = []
    i = 0
    while i < pop_size:
        # t=np.random.randint(0,2,chrom_len)*m
        t = np.array([0 for j in range(chrom_len)])
        x.append(t)
        # if check_constrain(t):

        i += 1

    return x


def calculate_fitness(chromosome, c, a, m, p, C, A):
    # calculate the fitness value of a chromosome
    x = chromosome
    cost = np.dot(x, c)
    area = np.dot(x, a)
    profit = np.dot(x, p)
    if cost > C or area > A or np.any((x > 0) & (x < m)):
        return -1
    return profit


def select_parents(population, fitness_vals, num_parents_rate):
    # select the best num_parents individuals as parents
    num_parents = int(len(population)*0.1)
    parent_indices = np.argsort(fitness_vals)[-num_parents:]
    return [population[i] for i in parent_indices]


def crossover(parents, offspring_size):
    # generate offspring by cross over parents
    offspring = []
    for i in range(offspring_size):
        parent1, parent2 = random.sample(parents, 2)
        cut_point = random.randint(0, len(parent1) - 1)
        offspring.append(np.hstack((parent1[:cut_point], parent2[cut_point:])))
    # return offspring
    filtered_offspring = [x for x in offspring if check_constrain(x)]
    return filtered_offspring


def mutation(offspring, mutation_prob):
    # mutate the offspring with probability mutation_prob
    for i in range(len(offspring)):
        for j in range(len(offspring[i])):
            if random.random() < mutation_prob:
                offspring[i][j] += random.randint(-max_m, max_m)
                offspring[i][j] = offspring[i][j] * (offspring[i][j] >= m[j])
    # return offspring
    filtered_offspring = [x for x in offspring if check_constrain(x)]
    return filtered_offspring


def genetic_algorithm(c, a, m, p, C, A, pop_size, chrom_len, num_parents_rate, offspring_size, mutation_prob,
                      num_generations):
    # main function to run the genetic algorithm
    record = []
    population = generate_population(pop_size, chrom_len)
    # print(population[:5])
    for i in tqdm(range(num_generations)):
        fitness_vals = [calculate_fitness(chrom, c, a, m, p, C, A) for chrom in population]
        # print("Gen: ", i, ": ", np.max(fitness_vals))
        parents = select_parents(population, fitness_vals, num_parents_rate)
        offspring = crossover(parents, offspring_size)
        offspring = mutation(offspring, mutation_prob)
        population = population + offspring
        # select best chromosome for the next generation
        key = lambda x : calculate_fitness(x, c, a, m, p, C, A)
        population.sort(key=key, reverse = True)
        population = population[:pop_size]
        record.append(max(fitness_vals))
    with open("record_{0}_{1}.pickle".format(chrom_len, pop_size), "wb") as file:
        pickle.dump(record, file)

    return population[np.argmax(fitness_vals)]


def append_new_line(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)


# Example usage
res = []
runtime = []
for i in [20, 40, 60, 80, 100]:
    N, A, C, c, a, f, m = load_data(os.path.join(test_path, str(i) + ".txt"))
    max_m = np.max(m)
    pop_size = 2000
    chrom_len = N
    num_parents_rate = 0.1
    offspring_size = 10
    mutation_prob = 0.2
    num_generations = 10000

    start = time.time()
    best_chromosome = genetic_algorithm(c, a, m, f, C, A, pop_size, chrom_len, num_parents_rate, offspring_size,
                                        mutation_prob, num_generations)
    end = time.time()
    append_new_line('res.txt', str(np.sum(best_chromosome * f)))
    append_new_line('time.txt', str(end - start))

