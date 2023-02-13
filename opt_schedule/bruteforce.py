import numpy as np
import time
def load_data(path='./testcase\ for\ Truong/3.txt'):
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
    global c,A,C,a
    cost=np.sum(inputs*c)
    area=np.sum(inputs*a)
    if cost>C or area>A:
        return False
    return True

def solve(inputs,i):
    global profit
    global amin,cmin,mmin,fmax,N,A,C,c,f,m,a
    
    cur=np.sum(inputs*f)
    
    if not check_constrain(inputs):
        return
    
    xh=min(int((A-np.sum(inputs*a))/amin[i]),int((C-np.sum(inputs*c))/cmin[i]))
    cut_heuristic=xh*(xh>=mmin[i])*fmax[i]+cur
    
    if cut_heuristic< profit:
        return
    if profit<cur:
        profit=cur
        
    if time.time()-init>300:
        return
    for k in range(i,len(inputs)):
        
        if inputs[k]==0:
            inputs[k]=m[k]
        else:
            inputs[k]+=1
        
        
        solve(inputs,k)
            
        if inputs[k]==m[k]:
            inputs[k]=0
        else:
            inputs[k]-=1
    return 
profit=0
res_x=[]
iter=0
import time
import matplotlib.pyplot as plt
import os
""
files=sorted(os.listdir('./testcase for Truong'))
list_testcase=[file for file in files if file.endswith('txt')]
pivot=[]
res=[]
time_stream=[]
testcases=[]

for testcase in list_testcase:
    
    target='testcase for Truong/'+testcase
    N,A,C,c,a,f,m=load_data(target)
    init=time.time()
    x=np.zeros_like(c)
    f=np.array(f)
    c=np.array(c)
    a=np.array(a)
    m=np.array(m)
    amin=np.zeros_like(c)
    cmin=np.zeros_like(c)
    mmin=np.zeros_like(c)
    fmax=np.zeros_like(c)
    amin[-1]=a[-1]
    cmin[-1]=c[-1]
    mmin[-1]=m[-1]
    fmax[-1]=f[-1]
    for i in range(2,len(c)+1):
        amin[-i]=min(a[-i],amin[-i+1])
        fmax[-i]=max(f[-i],fmax[-i+1])
        mmin[-i]=min(m[-i],mmin[-i+1])
        cmin[-i]=min(c[-i],cmin[-i+1])
    print(amin)
    profit =0
    solve(x,0)
    timecost=time.time()-init
    
    with open('bruteforcetest.txt','a+') as f:
        print("writing testcase"+testcase)
        base,_=os.path.splitext(testcase)
        s=base +'\t'+str(N)+'\t'+str(profit)+'\t'+str(timecost)+'\n'
        f.writelines(s)
