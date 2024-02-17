"""Task 4"""
class Wheels:
    """Wheels"""
    def __init__(self, number_of_wheels):
        self.number_of_wheels = number_of_wheels

    def rotate(self):
        """Rotates the wheels"""
        print("Wheels are rotating.")


class Engine:
    """Engine"""
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        """Starts the engine"""
        print("Engine started.")

    def stop(self):
        """Stops the engine"""
        print("Engine stopped.")


class Doors:
    """Doors"""
    def __init__(self, number_of_doors):
        self.number_of_doors = number_of_doors

    def open(self):
        """Opens the doors"""
        print("Doors are opening.")

    def close(self):
        """Closes the doors"""
        print("Doors are closing.")


class Car(Wheels, Engine, Doors):
    """Car"""
    def __init__(self, number_of_wheels, horsepower, number_of_doors):
        Wheels.__init__(self, number_of_wheels)
        Engine.__init__(self, horsepower)
        Doors.__init__(self, number_of_doors)

    def drive(self):
        """Starts a car"""
        print("Car is being driven.")
