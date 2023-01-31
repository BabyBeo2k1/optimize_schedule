class graph:
    e=[]
    n=0
    def __init__(self, n):
        self.n=n
    def gen(self,seed):
        random.seed(seed)
        e_size=random.randint(1,self.n*(self.n-1)/2)
        for i in range(e_size):
            end=random.randint(1,n+1)
            start=random.randint(1,n+1)
            cost=random.randint(1,n)
            if start!=end:
                self.e.append((end,start,cost))
    


            