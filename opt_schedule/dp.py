import os
import time
import numpy as np
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
def dynamic(N,A,C,c,a,f,m):
    global tle
    dp=np.zeros((N+1,A+1,C+1))-1
    
    tle=False
    init_time=time.time()
    dp[0][0][0]=0
    for i in range(N):
        for x in range(A+1):
            for y in range(C+1):
                if time.time()-init_time>300:
                    tle=True
                    return np.max(dp)
                if dp[i][x][y] >= 0:
                    dp[i + 1][x][y]=max((dp[i + 1][x][y], dp[i][x][y]))
                t=m[i]
                while t * a[i ] + x <= A and t * c[i ] + y <= C:
                    dp[i + 1][t * a[i ] + x][t * c[i ] + y]=max(dp[i + 1][t * a[i ] + x][t * c[i ] + y],dp[i][x][y] + t * f[i ])
                    t+=1
    return np.max(dp)
def record():
    global profit, file,tle,tclock
    with open('dp_result.txt','a+') as f:
        base,_=os.path.splitext(file)
        note=str(base)+'\t'+ str(profit) +'\t'
        if tle:
            note+="tle"
        else:
            note+=str(time.time()-tclock)
        f.writelines(note+'\n')


for file in sorted(os.listdir('testcase for Truong')):
    if file.endswith('txt'):
        N,A,C,c,a,f,m=load_data('testcase for Truong/'+file)
        tclock=time.time()
        profit =dynamic(N,A,C,c,a,f,m)
        record()
    