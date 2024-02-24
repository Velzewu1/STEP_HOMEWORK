"""Task 4"""
class Flat:
    """Flat"""
    def __init__(self, area, price) -> None:
        self.area = area
        self.price = price

    def __eq__(self, other):
        if self.area == other.area:
            return True
        else:
            return False
    def __ne__(self, other):
        if self.area != other.area:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.price >= other.price:
            return True
        else:
            return False
    def __le__(self, other):
        if self.price <= other.price:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.price > other.price:
            return True
        else:
            return False
    def __lt__(self, other):
        if self.price < other.price:
            return True
        else:
            return False
    