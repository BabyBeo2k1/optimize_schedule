import numpy as np
import time
conditions=np.loadtxt('test.txt', delimiter=' ').T
A=10e5
C=10e3
c= conditions[0]
a=conditions[1]
f=conditions[2]
m=conditions[3]
profit=0
def check_constrain(inputs):
    cost=np.sum(inputs*(inputs>=m)*c)
    area=np.sum((inputs*(inputs>=m))*a)
    if cost>C or area>A:
        return False
    return True

def solve(inputs):
    global profit
    if not check_constrain(inputs):
        return profit
    cur=np.sum((inputs*(inputs>=m))*f)
    if profit > cur:
        cur=profit
    start=time.time()

    for i in range(len(inputs)):
        inputs[i]+=1
        end=time.time()
        if end-start>300:
            return profit
        profit=max(cur,solve(inputs))

        inputs[i]-=1
    return profit
x=np.zeros_like(c)+4
#print(solve(x))
test=np.sum((x*(x>=m))*c)
print(test)
print(solve(x))