import numpy as np
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

def solve(inputs):
    global profit
    global tclock,tle
    
    cur=np.sum(inputs*f)
    if profit<cur:
        profit=cur
        res_x=inputs
    #eval.append(profit)
    if time.time()-tclock>300:
        tle=True
        return
    for i in range(len(inputs)):
        
        if inputs[i]==0:
            inputs[i]=m[i]
        else:
            inputs[i]+=1
        if check_constrain(inputs):
            
            solve(inputs)
            
        if inputs[i]==m[i]:
            inputs[i]=0
        else:
            inputs[i]-=1
    return 
def record():
    global profit, file,tle,tclock
    with open('bruteforce_result.txt','a+') as f:
        base,_=os.path.splitext(file)
        note=str(base)+'\t'+ str(profit) +'\t'
        if tle:
            note+="tle"
        else:
            note+=str(time.time()-tclock)
        f.writelines(note+'\n')




#print(solve(x))



eval=[]
"""import matplotlib.pyplot as plt
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(num, eval, 'g-')
ax2.plot(num, time_stream, 'b-')

ax1.set_xlabel('X data')
ax1.set_ylabel('best profit', color='g')
ax2.set_ylabel('time', color='b')


plt.show()"""

#read all files
for file in sorted(os.listdir('testcase for Truong')):
    if file.endswith('txt'):
        profit =0
        tle=False
        N,A,C,c,a,f,m=load_data('testcase for Truong/'+file)
        tclock=time.time()
        init_input=np.zeros_like(c)
        solve(init_input)
        record()
        continue