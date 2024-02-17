"""Task 3"""
class Square:
    """Square"""
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        """Calculates the area of the square"""
        return self.side_length ** 2


class Circle(Square):
    """Circle"""
    def __init__(self, diameter):
        super().__init__(side_length=diameter)
        self.diameter = self.side_length

    def area(self):
        """Calculates the area of the circle"""
        return 3.14 * (self.diameter / 2)**2
    