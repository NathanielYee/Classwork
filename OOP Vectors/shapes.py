'''

'''

class Shape:
    '''The base of our shape hierarchy'''
    def __init__(self,name):
        self.name = name
        self.xpos = 0
        self.ypos = 0

    def get_position(self):
        return self.xpos, self.ypos

    def move(self, x, y):
        '''Move the location of the shape by some delta'''
        self.xpos += x
        self.ypos += y

    def __repr__(self):
        return self.name + "(shape) @" +str(self.get_position())


class Circle(Shape):
    '''A circle is a type of shape'''
    def __init__(self,name,radius):
        # Instantiate (construct) the parent class (Super refrences parent object)
        super().__init__(name)
        #locallyt set the radius
        self.radius = radius
    def __repr__(self):
        return self.name + "circle @" + str(self.get_position()), 'withradius= '+ int(self.radius)
        #return super().__repr__() + 'with radius = '+str(self.radius)
    pass

    def area(self,radius):
        return 3.14 * (radius **2)

class Square(Shape):
    '''A square is a type of shape'''
    pass



def main():
    blob = Shape('blob')
    blob.move(2,3)
    blob.move(0,-1)
    print(blob)

    c = Circle('Circle of Life', 4)
    c.move(5,5)
    print(c)

if __name__ == '__main__':
    main()