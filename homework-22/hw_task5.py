"""Task 5"""

class Shape:
    """Base class"""
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def Show(self):
        """Shows properties"""
        print(f"Coordinates: ({self.x}, {self.y})")

    def Save(self, filename):
        """Saves info to a file"""
        with open(filename, 'a', encoding="utf-8") as f:
            f.write(f"{type(self).__name__} {self.x} {self.y}\n")

    @classmethod
    def Load(filename):
        """Loads info from a file """
        with open(filename, 'r', encoding="utf-8") as file:
            for line in file:
                info = line.strip()
                if info == "Square":
                    return "it is square"
                elif info == "Rectangle":
                    return"it is Circle"
                elif info == "Rectangle":
                    return"it is Circle"
                elif info == "Ellipse":
                    return"it is Ellipse"
                else:
                    continue


class Square(Shape):
    """Square"""
    def __init__(self, x, y, side_length):
        super().__init__(x, y)
        self.side_length = side_length
    
    def Show(self):
        """Shows properties"""
        super().Show()
        print("Type: Square")
        print(f"Side Length: {self.side_length}")


class Rectangle(Shape):
    """Rectangle"""
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height
    
    def Show(self):
        """Shows properties"""
        super().Show()
        print("Type: Rectangle")
        print(f"Width: {self.width}")
        print(f"Height: {self.height}")


class Circle(Shape):
    """Circle"""
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
    
    def Show(self):
        """Shows properties"""
        super().Show()
        print("Type: Circle")
        print(f"Radius: {self.radius}")


class Ellipse(Shape):
    """Ellipse"""
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height
    
    def Show(self):
        """Shows properties"""
        super().Show()
        print("Type: Ellipse")
        print(f"Width: {self.width}")
        print(f"Height: {self.height}")
    