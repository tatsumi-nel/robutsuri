import math

class Vector(tuple):

    def __init__(self):
        self.data = [0.0, 0.0]
        super()

    def __abs__(self):
        """it returns the magnitude of vector"""
        return math.sqrt(sum([x*x for x in self]))

    def norm(self):
        """it returns the normalized vector"""
        a = self.__abs__()
        return Vector([x/a for x in self])

    def __add__(self, other):
        if isinstance(other, Vector):
            if (len(self) == len(other)):
                return Vector([x + y for x, y in zip(self, other)])
            else:
                raise ValueError, "Same dimension is required for the operation."
        else:
            raise TypeError, "Vector is required."

    def __sub__(self, other):
        if isinstance(other, Vector):
            if (len(self) == len(other)):
                return Vector([x - y for x, y in zip(self, other)])
            else:
                raise ValueError, "Same dimension is required for the operation."
        else:
            raise TypeError, "Vector is required."
        
    def __mul__(self, factor):
        if isinstance(factor, float):
            raise TypeError, "a float value is required."
        return Vector([x * factor for x in self])
    
    def __rmul__(self, factor):
        return self.__mul__(self,factor)

    



