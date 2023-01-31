import numpy as np
def data():
    path='test.txt'
    conditions=np.loadtxt(path, delimiter=' ').T
    A=10e5
    C=10e3
    c= conditions[0]
    a=conditions[1]
    f=conditions[2]
    m=conditions[3]
    profit=0
    return data
def check_constrain(inputs):
    cost=np.sum(inputs*(inputs>=m)*c)
    area=np.sum((inputs*(inputs>=m))*a)
    if cost>C or area>A:
        return False
    return True
