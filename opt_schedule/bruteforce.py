import numpy as np
import time
def load_data(path='./testcase/3.txt'):
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
N,A,C,c,a,f,m=load_data()

def check_constrain(inputs):
    cost=np.sum(inputs*c)
    area=np.sum(inputs*a)
    if cost>C or area>A:
        return False
    return True
eval=[]
def solve(inputs,init_time):
    global profit
    global iter,res_x
    time_constrain=time.time()
    cur=np.sum(inputs*f)
    
    if profit<cur:
        profit=cur
        res_x=inputs
    eval.append(profit)
    if time.time()-init_time>10:
        return
    for i in range(len(inputs)):
        
        if inputs[i]==0:
            inputs[i]=m[i]
        else:
            inputs[i]+=1
        if check_constrain(inputs):
            
            solve(inputs,init_time)
            
        if inputs[i]==m[i]:
            inputs[i]=0
        else:
            inputs[i]-=1
    return 
profit=0
res_x=[]
iter=0
import time
import matplotlib.pyplot as plt
import os
files=(os.listdir('./testcase'))
list_testcase=[file for file in files[:20] if file.endswith('txt')]
pivot=[]
res=[]
time_stream=[]
testcases=[]

for testcase in list_testcase:
    
    target='testcase/'+testcase
    N,A,C,c,a,f,m=load_data(target)
    profit =0
    
    x=np.zeros_like(c)
    #print(solve(x))
    res_x=np.zeros_like(x)
    init=time.time()
    testcases.append(testcase)
    
    
    solve(x)
    timecost=time.time()-init
    time_stream.append(timecost)
    
    pivot.append(N)
    res.append(profit)
    with open('bruteforcetest.txt','a+') as f:
        print("writing testcase"+testcase)
        base,_=os.path.splitext(testcase)
        s=base +'\t'+str(N)+'\t'+str(profit)+'\t'+str(timecost)+'\n'
        f.writelines(s)

print(profit)
print(res_x)
num=np.arange(iter)
import matplotlib.pyplot as plt
plt.plot(num,eval)
#plt.show()