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

def calc_profit(x, f, c, a, A, C,m):
    profit = sum([f[i] * (x[i]>=m[i]) for i in range(len(x))])
    cost = sum([c[i] * (x[i]>=m[i]) for i in range(len(x))])
    area = sum([a[i] * (x[i]>=m[i]) for i in range(len(x))])
    if area > A or cost > C:
        return -1e9 # a very large negative number
    return profit

def hill_climbing(f, c, a, A, C, m, N, max_iters):
    x = [0 for i in range(N)] # initial solution
    best_profit = calc_profit(x, f, c, a, A, C,m)
    for i in range(max_iters):
        j = random.randint(0, N-1)
        d=0
        if x[j]==0:
            x[j]=m[j]
        else:
            d=random.randint(1,3)
            x[j]+=d# increase x[j] by 1
        print(x)
        profit = calc_profit(x, f, c, a, A, C,m)
        if profit > best_profit:
            best_profit = profit
        else:
            if x[j]==m[j]:
                x[j]=0
            else:
                x[j]-=d# decrease x[j] back to original value
    return x, best_profit

# Example usage

x, best_profit = hill_climbing(f, c, a, A, C, m, N, 10000)
print("Optimal solution: ", x)
print("Optimal profit: ", best_profit)
x=np.random.randint(low=10e4,high=10e5, size=(10,N))
print(check_constrain(x))    

    