import numpy as np
from tqdm import tqdm
def load_data(path='./testcase/9.txt'):
    with open(path, "r") as file:
            # read the file line by line
        lines = file.readlines()
        # convert each line to integer and append to the list
        conditions= [[int(i)for i in line.strip().split(' ')] for line in lines if len(line.strip())>0]

    N=conditions[0][0]
    A=conditions[0][1]
    C=conditions[0][2]
    c= conditions[1]
    a=conditions[2]
    f=conditions[3]
    m=conditions[4]
    return N,A,C,c,a,f,m


def check_constrain(inputs):
    cost=np.sum(inputs*c)
    area=np.sum(inputs*a)
    if cost>C or area>A:
        return False
    return True
eval=[]

def greedy_production_planning(N, c, a, f, m, A, C):
   
    
    res=[]
    res_p=[]
    timeconstrain=time.time()
    for k in tqdm(range(N)):

        remaining_area = A
        cost = 0
        profit=0
        x=np.zeros(N)
        for j in range(N):
            i=(k+j)%N
            if time.time()-timeconstrain>30:
                return res,res_p
            if cost + c[i]*m[i] <= C and a[i]*m[i] <= remaining_area:
                x[i] = m[i]
                cost += c[i] * x[i]
                profit += f[i] * x[i]
                remaining_area -= a[i] * x[i]
                
                while cost + c[i] <= C and a[i] <= remaining_area:
                    x[i] += 1
                    cost += c[i]
                    profit += f[i]
                    remaining_area -= a[i]
        res.append(x)
        res_p.append(profit)
    i_max=np.argmax(res_p)
    return res, res_p

import time
import matplotlib.pyplot as plt
import os
files=(os.listdir('./testcase'))
list_testcase=[file for file in files if file.endswith('txt')]
pivot=[]
res=[]
time_stream=[]
testcases=[]
for testcase in list_testcase:
    init=time.time()
    testcases.append(testcase)
    target='testcase/'+testcase
    N,A,C,c,a,f,m=load_data(target)
    _,res_p=greedy_production_planning(N,c,a,f,m,A,C)

    timecost=time.time()-init
    time_stream.append(timecost)
    id=np.argmax(res_p)
    pivot.append(N)
    res.append(np.max(res_p))
    with open('greedytest.txt','a+') as f:
        base,_=os.path.splitext(testcase)
        s=base +'\t'+str(N)+'\t'+str(np.max(res_p))+'\t'+str(timecost)+'\n'
        f.writelines(s)
#plt.show()
