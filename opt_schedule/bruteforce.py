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
    cost=np.sum(inputs*c)
    area=np.sum(inputs*a)
    if cost>C or area>A:
        return False
    return True

def solve(inputs):
    global profit
    
    
    cur=np.sum(inputs*f)
    profit=max(profit,cur)
    print(inputs)

    for i in range(len(inputs)):
        
        if inputs[i]==0:
            inputs[i]=m[i]
        else:
            inputs[i]+=1
        if check_constrain(inputs):
            print(inputs)
            solve(inputs)
        
        if inputs[i]==m[i]:
            inputs[i]=0
        else:
            inputs[i]-=1
    return
profit =0
x=np.zeros_like(c)
#print(solve(x))
test=np.sum((x*(x>=m))*f)
solve(x)
print(check_constrain(x+1))
print(profit)