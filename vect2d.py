 


class clsVect2D :
    __count = 0 
    def getCount(self):
        return self.__count
    def __init__(self,x =0 ,y=0 ):
        self.x = x
        self.y = y
        clsVect2D.__count += 1 
    
    # def __init__(self, vect2D):
    #     self.x = vect2D.x
    #     self.y = vect2D.y
    #     _count += 1 
    
    def toString(self):
        return "x = " + str(self.x) + "y = " + str(self.y)
    
    def equals(self, vect2D):
        return (self.x == vect2D.x and self.y == vect2D.y)
    
    def norme(self):
        return (self.x**2 + self.y**2)**1/2

    
