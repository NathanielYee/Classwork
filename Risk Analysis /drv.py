'''
Discrete Random Variable Object (DRV)
Nathaniel Yee
DS 2500
'''
import copy
import random as rnd
import seaborn as sns
import matplotlib.pyplot as plt

def E(X):
    return X.E()


class DRV:
    def __init__(self, dist=None):
        if dist is None:
            self.dist = {}
        else:
            self.dist = copy.deepcopy(dist) # setting up a dictionary to represent internal variable
    def random(self,k=1):
        '''Generate a random outcome according to the prob dist'''
        #@ k= # of outcomes returned as a list of k>1
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
        """Enables Z[i] ==> probability that Z  = X"""
        return self.dist.get(x,0.0)

    def __setitem__(self, x, p):
        '''Z[x] = p'''
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
    def applyscalar(self,a,op):
        '''Apply a binary operator to self and to the number a'''
        X = DRV()
        items = list(self.dist.items())
        for x,p in items:
            X[op(x,a)] += p
        return X

    def __add__(self, other):
        '''Add two drvs X + Y'''
        return self.apply(other, lambda x,y: x + y)

    def __sub__(self, other):
        '''Sub two drvs X + Y'''
        return self.apply(other, lambda x,y: x - y)

    def __mul__(self, other):
        '''Mult two drvs X * Y'''
        return self.apply(other,lambda x,y: x * y)

    def __truediv__(self, other):
        '''Div to drvs '''
        return self.apply(other,lambda x,y:x / y)

    def __radd__(self, a):
        '''Add a to a drv ex: a+x, y= a + X'''
        return self.applyscalar(a, lambda x,c: c+x)

    def __rsub__(self, a):
        '''Add a to a drv ex: a+x, y= a + X'''
        return self.applyscalar(a, lambda x,c: c-x)

    def __rmul__(self, a):
        '''Add a to a drv ex: a+x, y= a + X'''
        return self.applyscalar(a, lambda x,c: c*x)

    def plot(self):
        sample = self.random(k=10000);
        sns.displot(sample, kind='hist', stat='density')
        plt.show()

    def __repr__(self):
        '''Returns the drv as a printable string'''
        xp = sorted(list(self.dist.items()))
        rslt = ''
        for x, p in xp:
            rslt += str(x) + ' : ' + str(round(p,8)) + '\n'
        return rslt


def main():
    D6 = DRV({1:1/6,2:1/6,3:1/6,4:1/6,5:1/6,6:1/6}) # uniform dist of a 6 sided dice 1/6 prob
    print(D6.E())
    print(list(D6.dist.items()))
    print(D6.random(k=10))
    roll = D6 + D6
    print(roll)
    #roll.plot()
    score = 10 + D6
    print(score)
    score.plot()

if __name__ == '__main__':
    main()