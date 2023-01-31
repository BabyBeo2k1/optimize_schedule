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
    
    cost=np.sum(inputs*(inputs>=m)*c,axis=0)
    area=np.sum((inputs*(inputs>=m))*a,axis=0)
    x= np.logical_and(cost>C,area>A)
    return x

x=np.random.randint(low=10e4,high=10e5, size=(10,N))
print(check_constrain(x))    

    