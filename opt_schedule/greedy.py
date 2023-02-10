import numpy as np
from tqdm import tqdm
import time
import os
def load_data(path='test3.txt'):
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

def greedy_production_planning(N, c, a, f, m, A, C):
   
    
    res=[]
    res_p=[]
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
                    if time.time()-init_time>300:
                        tle=True
                        break
                    x[i] += 1
                    cost += c[i]
                    profit += f[i]
                    remaining_area -= a[i]
        res=max(res,profit)
    
    with open('heuristic_result.txt','a+') as f:
        base,_=os.path.splitext(file)
        note=str(base)+'\t'+ str(res) +'\t'
        if tle:
            note+="tle"
        else:
            note+=str(time.time()-init_time)
        f.writelines(note+'\n')
    return 
"""x=np.arange(0,N)"""
"""import matplotlib.pyplot as plt
res,res_p=greedy_production_planning(N,c,a,f,m,A,C)

fig, ax1 = plt.subplots()
"""
"""ax2 = ax1.twinx()
ax1.plot(x, res_p, 'g-')
ax2.plot(x, time_stream, 'b-')

ax1.set_xlabel('X data')
ax1.set_ylabel('best profit', color='g')
ax2.set_ylabel('time', color='b')

id=np.argmax(res_p)

print(res[id],res_p[id])
plt.show()
"""
for file in sorted(os.listdir('testcase for Truong')):
    if file.endswith('txt'):
        
        N,A,C,c,a,f,m=load_data('testcase for Truong/'+file)
        
        greedy_production_planning(N, c, a, f, m, A, C)
        