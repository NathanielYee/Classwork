'''
Discrete Random Variable Object (DRV)
Nathaniel Yee
DS 2500
'''
import copy
import random as rnd



class DRV:
    def __init__(self, dist=None):
        if dist is None:
            self.dist = {}
        self.dist = copy.deepcopy(dist) # setting up a dictionary to represent internal variable





def main():
    D6 = DRV({1:1/6,2:1/6,3:1/6,4:1/6,5:1/6,6:1/6}) # uniform dist of a 6 sided dice 1/6 prob

if __name__ == '__main__':
    main()