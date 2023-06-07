'''
Nathaniel Yee
June 5 2023
vector.py
description: simple vector class
'''
import math
class Vector:
    '''A simple vector class'''

    def __init__(self,*components):
        self._components = list(components)

    def mag(self):
        '''Magnitude of the vector |V| '''
        return sum([c ** 2 for c in self._components]) ** .5

    def dim(self):
        '''Dimensions of this vector'''
        return len(self._components)

    def __getitem__(self,idx):
        '''Use indexing (subscripting) to ith vector component '''
        return self._components[idx]

    def __add__(self, other):
        copy = self._components[:]
        for i in range(len(copy)):
            copy[i] = copy[i] + other[i] #fixed is ._components
        return Vector(*copy)

    def __mul__(self, other):
        if type(other) == Vector:
            return sum([self[i] * other[i] for i in range(self.dim())])
        elif type(other) == int or type(other) == float:
            scaled = [other * c for c in self]
            return Vector(*scaled) # convert list of scaled components into params

    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        return self + -other

    def cosine(self,other):
        #The cosine of the angle between two vectors
        #A dot B = |A| |B| cos(theta)
        return self * other / (self.mag() * other.mag())
    def angle(self,other):
        import math
        return math.acos(self.cosine(other)) * 180 / math.pi

    def __repr__(self):
        if self.dim() == 2:
            result = str(self._components[0]) +"i + " + str(self._components[1])+"j"
        elif self.dim() == 3:
            result = str(self._components[0]) +"i + " + str(self._components[1])+"j + " + str(self._components[2])+"k"
        else:
            result = str(self._components)
        return result


def main():
    ''' Test methods on the vector class '''
    v = Vector(3, 4, 5)
    u = Vector(1,2,3)
    w = Vector(10, 2,-8)

    print(u, u.dim(), u.mag())
    print(v,v.dim(),v.mag())
    print(w,w.dim(),w.mag())

    z = u + v
    print("z:",z)

    x = u+v+w
    print('x:',x)

    print("slicing", x[1:])

    # u dot v = 1*3 + 2*4 + 3*5
    dp = u * v
    print("dot product of ", u, 'and', v,":", dp)

    print("u-v", u,v,u-v)

    i = Vector(1,0,0)
    j = Vector(0,1,0)
    print(i.angle(i))
 #   my_object = Classname(initial_parameters to construct that instance)

if __name__ == "__main__":
    main()