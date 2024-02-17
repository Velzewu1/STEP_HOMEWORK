"""Task 1"""
class Device:
    """Parent class for devices"""
    def __init__(self, brand, model, power_consumption):
        self.brand = brand
        self.model = model
        self.power_consumption = power_consumption

    def turn_on(self):
        """Turn on device"""
        print(f"{self.brand} {self.model} is now turned on.")

    def turn_off(self):
        """Turn off device"""
        print(f"{self.brand} {self.model} is now turned off.")


class CoffeeMachine(Device):
    """Coffe machine"""
    def __init__(self, brand, model, power_consumption, coffee_type):
        super().__init__(brand, model, power_consumption)
        self.coffee_type = coffee_type

    def make_coffee(self):
        """Makes a coffe"""
        print(f"Making {self.coffee_type} coffee with {self.brand} {self.model}.")


class Blender(Device):
    """Blender"""
    def __init__(self, brand, model, power_consumption, speed_level):
        super().__init__(brand, model, power_consumption)
        self.speed_level = speed_level

    def blend(self):
        """Blends"""
        print(f"Blending with {self.brand} {self.model} at speed level {self.speed_level}.")


class MeatGrinder(Device):
    """Meat Crinder"""
    def __init__(self, brand, model, power_consumption, grinder_type):
        super().__init__(brand, model, power_consumption)
        self.grinder_type = grinder_type

    def grind_meat(self):
        """Grinds meat"""
        print(f"Grinding meat with {self.brand} {self.model} ({self.grinder_type}).")
