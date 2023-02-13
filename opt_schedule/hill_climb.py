import os
import numpy as np
import time
from tqdm import tqdm
import random
import pickle

test_path = './testcase for Truong'

def load_data(path):
    with open(path, "r") as file:
        # read the file line by line
        lines = file.readlines()
        # convert each line to integer and append to the list
        conditions = [[int(i) for i in line.strip().split(' ')] for line in lines if len(line.strip())]

    N = conditions[0][0]
    A = conditions[0][1]
    C = conditions[0][2]
    c = conditions[1]
    a = conditions[2]
    f = conditions[3]
    m = conditions[4]
    return N, A, C, c, a, f, m


def calc_profit(x, f, c, a, A, C, m):
    profit = sum([f[i] * x[i] * (x[i] >= m[i]) for i in range(len(x))])
    cost = sum([c[i] * x[i] * (x[i] >= m[i]) for i in range(len(x))])
    area = sum([a[i] * x[i] * (x[i] >= m[i]) for i in range(len(x))])
    if area > A or cost > C:
        return -1e9  # a very large negative number
    return profit


def hill_climbing(f, c, a, A, C, m, N, max_iters, max_range):
    record = []
    x = [0 for i in range(N)]  # initial solution
    best_profit = calc_profit(x, f, c, a, A, C, m)
    for i in tqdm(range(max_iters)):
        j = random.randint(0, N - 1)
        old_val = x[j]
        d = random.randint(1, max_range + 1)
        if x[j] == 0:
            if np.random.rand() <= 0.5:
                x[j] = m[j] + d
        else:
            x[j] += d

        profit = calc_profit(x, f, c, a, A, C, m)
        if profit > best_profit:
            best_profit = profit
        else:
            x[j] = old_val  # decrease x[j] back to original value
        record.append(best_profit)
    with open("record_{0}_{1}.pickle".format(N, max_range), "wb") as file:
        pickle.dump(record, file)

    return x, best_profit


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


max_iter = 10000

for i in [20, 40, 60, 80, 100]:
    start = time.time()
    N, A, C, c, a, f, m = load_data(os.path.join(test_path, str(i) + ".txt"))
    max_range = 8
    x, best_profit = hill_climbing(f, c, a, A, C, m, N, max_iter, max_range)
    end = time.time()
    append_new_line('res.txt', str(best_profit))
    append_new_line('time.txt', str(end - start))

