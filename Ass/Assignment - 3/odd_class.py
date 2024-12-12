class odd:
    def __init__(self,max=0):
        self.max=max
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        res=None
        if self.n <= self.max:
            if self.n%2!=0:
                res=self.n
            self.n+=1
            return res
        else:
            raise StopIteration
        
o=odd(5)
for i in o:
    print(i)