"""Task 2"""
class Ship:
    """Parent class for Ships"""
    def __init__(self, model, size, speed, capacity):
        self.size = size
        self.model = model
        self.speed = speed
        self.capacity = capacity

    def set_sail(self):
        """Turn on Ship"""
        print(f"{self.model} is set sailed.")


class Frigate(Ship):
    """Frigate"""
    def __init__(self, model, size, speed, capacity, sail_quantity):
        super().__init__(model, size, speed, capacity)
        self.sail_quantity = sail_quantity

    def open_sails(self):
        """Open sails"""
        print(f"All the {self.sail_quantity} sails on frigate {self.model} are opened.")


class Destroyer(Ship):
    """Destroyer"""
    def __init__(self, model, size, speed, capacity, torpedoes_quantity):
        super().__init__(model, size, speed, capacity)
        self.torpedoes_quantity = torpedoes_quantity

    def torpedo_salvo(self):
        """Launch torpedoes"""
        print(f"Launching all {self.torpedoes_quantity} torpedoes from destroyer {self.model}.")


class Cruiser(Ship):
    """Cruiser"""
    def __init__(self, model, size, speed, capacity, cannon_quantity):
        super().__init__(model, size, speed, capacity)
        self.cannon_quantity = cannon_quantity

    def cannon_fire(self):
        """Fires from cannons"""
        print(f"Firing all {self.cannon_quantity} cannons from {self.model}.")
