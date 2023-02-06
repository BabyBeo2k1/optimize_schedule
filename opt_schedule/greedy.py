import numpy as np
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
    cost=np.sum(inputs*c)
    area=np.sum(inputs*a)
    if cost>C or area>A:
        return False
    return True
eval=[]

def greedy_production_planning(N, c, a, f, m, A, C):
   
    
    res=[]
    res_p=[]
    for k in range(N):

        remaining_area = A
        cost = 0
        profit=0
        x=np.zeros(N)
        for j in range(N):
            i=(k+j)%N
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
x=np.arange(0,N)
import matplotlib.pyplot as plt
res,res_p=greedy_production_planning(N,c,a,f,m,A,C)
id=np.argmax(res_p)
plt.plot(x,res)
print(res[id],res_p[id])
#plt.show()
