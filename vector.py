'''This program does some computations on vectors in 2D without 
using numpy'''

class vector(object):
    
    #vectors can be initialized as a = vector(x_component, y_component). Default = (0,0)
    def __init__(self, x = 0, y = 0):
        self.x, self.y = x, y

    #if a = vector(2,3), print(a) gives output <2,3>
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    
    #a==b compares two vectors
    def __eq__(self, other):
        if self.x==other.x and self.y==other.y:
            return True
        else:
            return False
    
    #a!=b compares two vctors
    def __ne__(self,other):
        if(self==other):
            return False
        else:
            return True
    
    #-a negates each component
    def __neg__(self):
        return vector(-self.x, -self.y)

    #a + b adds two vectors
    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)
    
    #a-b subtracts two vectors
    def __sub__(self, other):
        return vector(self.x - other.x, self.y - other.y)

    #abs(a) gives the length of a
    def __abs__(self):
        return ((self.x)**2 + (self.y^2))**0.5
    
    #a*b does scalar multiplication if b is vector or scalar
    def __mul__(self, other):
        if isinstance(other, vector):
            return other.x*self.x + other.y*self.y
        elif type(other)!='str':
            return vector(other*self.x, other*self.y)

    #cross(a,b) does vector product
    def cross(self, other):
        return vector(self.x*other.y - other.x*self.y)
    
    #measure distance between heads of two vectors
    def dist(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    #a**n just repeats scalar multiplication of a with itself
    def __pow__(self, c):
        return vector(self.x**c, self.y**c)

    #converts vector to a complex number
    def __complex__(self):
        return complex(self.x,self.y)