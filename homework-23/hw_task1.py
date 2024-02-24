"""Task1"""
import math


class Circle:
    """Circle"""
    def __init__(self, radius) -> None:
        """Initialize"""
        self.rad = radius
        self.circumference = self.rad * 2 *  math.pi


    def __eq__(self, other):
        """=="""
        if self.rad == other.rad:
            return True
        else:
            return False



    def __lt__(self, other):
        """<"""
        if self.rad < other.rad:
            return True
        elif self.rad >= other.rad:
            return False
        else:
            return False 
       
    def __gt__(self, other):
        """>"""
        if self.rad <= other.rad:
            return False
        elif self.rad > other.rad:
            return True       


    def __le__(self, other):
        """<="""
        if self.rad <= other.rad:
            return True
        else:
            return False       
             
    def __ne__(self, other):
        """>="""
        if self.rad >= other.rad:
            return True
        else:
            return False


    def __add__(self, other):
        """+"""
        return self.rad + other
    
    def __sub__(self, other):
        """-"""
        return self.rad - other


    def __iadd__(self, other):
        """+="""
        self.rad += other
        self.circumference = self.rad * 2 *  math.pi
    
    def __isub__(self, other):
        """-="""
        self.rad -= other
        self.circumference = self.rad * 2 *  math.pi

if __name__ == "__main__":
    circ1 = Circle(5)
    circ2 = Circle(4)

    print(circ1 - circ2)