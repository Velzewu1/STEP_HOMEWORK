"""Task 3"""
class Airplane:
    """Airplane"""
    def __init__(self, plane_type, max_value, cur_value) -> None:
        self.type = plane_type
        self.max = max_value
        self.cur = cur_value

    def __eq__(self, other):
        if self.type == other.type:
            return True

    def __add__(self, num):
        self.cur += num
        return self.cur

    def __iadd__(self, num):
        self.cur += num
        return self.cur

    def __sub__(self, num):
        self.cur -= num
        return self.cur

    def __isub__(self, num):
        self.cur -= num
        return self.cur

    def __lt__(self, other):
        if self.max < other.max:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.max > other.max:
            return True
        else:
            return False

    def __le__(self, other):
        if self.max <= other.max:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.max >= other.max:
            return True
        else:
            return False