'''
Discrete Random Variable Object (DRV)
Nathaniel Yee
DS 2500
'''
import copy
import random as rnd

def E(X):
    return X.E()


class DRV:
    def __init__(self, dist=None):
        if dist is None:
            self.dist = {}
        self.dist = copy.deepcopy(dist) # setting up a dictionary to represent internal variable
    def random(self,k=1):
        '''Generate a random outcome according to the prob dist'''
        outcomes = list(self.dist.keys())
        probs = list(self.dist.values())
        rslt = rnd.choices(outcomes,probs,k=k)
        if k == 1:
            return rslt[0]
        else:
            return rslt
    def E(self):
        return sum([x*p for x,p in self.dist.items()])

    def __getitem__(self, x):
        return self.dist.get(x,0.0)

    def __setitem__(self, x, p):
        self.dist[x] = p
    def apply(self, other, op):
        '''Apply a binary operator (+,-,*) to self and other across  every possible pair of outcomes'''
        X = DRV()
        items = list(self.dist.items())
        oitems = list(other.dist.items())
        for x, px in items:
            for y, py in oitems:
                X[op(x,y)] += px * py
        return X

    def __add__(self, other):
        '''Add two drvs X + Y'''
        return self.apply(other, lambda x,y: x+y)


def main():
    D6 = DRV({1:1/6,2:1/6,3:1/6,4:1/6,5:1/6,6:1/6}) # uniform dist of a 6 sided dice 1/6 prob
    print(D6.E())
    print(list(D6.dist.items()))
    print(D6.random(k=10))
    roll = D6 + D6
    print(roll.dist)

if __name__ == '__main__':
    main()