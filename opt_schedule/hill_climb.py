import numpy as np
import time
from tqdm import tqdm
def load_data(path='test3.txt'):
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
    profit = sum([f[i] *x[i]* (x[i]>=m[i]) for i in range(len(x))])
    cost = sum([c[i] * x[i]*(x[i]>=m[i]) for i in range(len(x))])
    area = sum([a[i] * x[i]*(x[i]>=m[i]) for i in range(len(x))])
    if area > A or cost > C:
        return -1e9 # a very large negative number
    return profit
eval=[]
def hill_climbing(f, c, a, A, C, m, N, max_iters):
    x = [0 for i in range(N)] # initial solution
    best_profit = calc_profit(x, f, c, a, A, C,m)
    for i in tqdm(range(max_iters)):
        
        j = random.randint(0, N-1)
        d=0
        while d==0:
            d=random.randint(-1,3)
        if x[j]==0:
            if d<2:
                x[j]=m[j]
                d=m[j]
            else:
                x[j]=m[j]+1
                d=m[j]+1
        else:
            if x[j]+d<m[j]:
                d=-x[j]
                x[j]=0
            else:
                x[j]+=d
                                
            # increase x[j] by 1
        
        profit = calc_profit(x, f, c, a, A, C,m)
        if profit > best_profit:
            best_profit = profit
            
        else:
            x[j]-=d# decrease x[j] back to original value
        if i%10==0:
                eval.append(best_profit)
                
    return x, best_profit

# Example usage
max_iter=1000000
iter=np.arange(max_iter/10)
import matplotlib.pyplot as plt
x, best_profit = hill_climbing(f, c, a, A, C, m, N, max_iter)

plt.plot(iter,eval)

print("Optimal solution: ", x)
print("Optimal profit: ", best_profit)
#plt.show()
    