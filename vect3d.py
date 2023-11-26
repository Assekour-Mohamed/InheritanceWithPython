from vect2d import clsVect2D 
    
class clsVect3D(clsVect2D):
    def __init__(self, x =1, y = 1, z=1):
        super().__init__(x,y)
        self.z = z
    # def __init__(self, vect3D):
    #     super().__init__(vect3D )
    #     self.z = vect3D.z
    
    def toString(self):
        return "x = " + str(self.x) + " y = " + str(self.y)+ " z = " + str(self.z)
    
    def equals(self, vect3D):
        return (self.x == vect3D.x and self.y == vect3D.y and self.z == vect3D.z)
    
    def norme(self):
        return (self.x**2 + self.y**2 + self.z **2)**1/2
  
