import numpy as np
import time
def load_data(path='test.txt'):
    with open(path, "r") as file:
            # read the file line by line
        lines = file.readlines()
        # convert each line to integer and append to the list
        conditions= [[int(i)for i in line.strip().split(' ')] for line in lines]

    N=conditions[0][0]
    A=conditions[0][1]
    C=conditions[0][2]
    c= conditions[1]
    a=conditions[2]
    f=conditions[3]
    m=conditions[4]
    return N,A,C,c,a,f,m
N,A,C,c,a,f,m=load_data()

def check_constrain(inputs):
    cost=np.sum(inputs*(inputs>=m)*c)
    area=np.sum((inputs*(inputs>=m))*a)
    if cost>C or area>A:
        return False
    return True
import random


def generate_population(pop_size, chrom_len):
    # generate a population of pop_size individuals, each with a chromosome of length chrom_len
    x=[]
    i=0
    while i<pop_size:
        t=np.random.randint(0,2,chrom_len)*m
        if check_constrain(t):
            x.append(t)
            i+=1
        
    return x

def calculate_fitness(chromosome, c, a, m, p, C, A):
    # calculate the fitness value of a chromosome
    x = chromosome 
    cost = np.dot(x, c)
    area = np.dot(x, a)
    profit = np.dot(x, p)
    if cost > C or area > A or any(x < m):
        return -1
    return profit

def select_parents(population, fitness_vals, num_parents):
    # select the best num_parents individuals as parents
    parent_indices = np.argsort(fitness_vals)[-num_parents:]
    return [population[i] for i in parent_indices]

def crossover(parents, offspring_size):
    # generate offspring by cross over parents
    offspring = []
    for i in range(offspring_size):
        parent1, parent2 = random.sample(parents, 2)
        offspring.append(np.hstack((parent1[:len(parent1)//2], parent2[len(parent2)//2:])))
    return offspring

def mutation(offspring, mutation_prob):
    # mutate the offspring with probability mutation_prob
    for i in range(len(offspring)):
        for j in range(len(offspring[i])):
            if random.random() < mutation_prob:
                offspring[i][j]+= random.randint(-1,5)
                offspring[i][j]=offspring[i][j]*(offspring[i][j]>=m[j])
    return offspring

def genetic_algorithm(c, a, m, p, C, A, pop_size, chrom_len, num_parents, offspring_size, mutation_prob, num_generations):
    # main function to run the genetic algorithm
    population = generate_population(pop_size, chrom_len)
    print(population[:5])
    for i in range(num_generations):
        fitness_vals = [calculate_fitness(chrom, c, a, m, p, C, A) for chrom in population]
        parents = select_parents(population, fitness_vals, num_parents)
        offspring = crossover(parents, offspring_size)
        offspring = mutation(offspring, mutation_prob)
        population = parents + offspring
    return population[np.argmax(fitness_vals)]

# Example usage

pop_size = 50
chrom_len = 5
num_parents = 100
offspring_size = 100
mutation_prob = 0.2
num_generations = 10000


best_chromosome = genetic_algorithm(c, a, m, f, C, A, pop_size, chrom_len, num_parents,offspring_size,mutation_prob,num_generations)
print(best_chromosome,(np.sum(best_chromosome*f)))