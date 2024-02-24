"""Task 2"""
class Complex:
    """Complex number"""
    def __init__(self, first_num, second_num):
        self.value = complex(first_num, second_num)

    def __add__(self, other):
        self.value += other.value
        return self.value

    def __sub__(self, other):
        self.value -= other.value
        return self.value

    def __mul__(self, other):
        self.value *= other.value
        return self.value

    def __truediv__(self, other):
        self.value /= other.value
        return self.value

if __name__ == "__main__":
    a = Complex(1, 2)
    b = Complex(5, 2)
    print(a / b)
