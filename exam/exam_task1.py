"""Pizza delivery"""
class Pizza:
    """Pizza"""
    def __init__(self, name, dough, sauce, toppings, price) -> None:
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings
        self.price = price

    def prepare(self):
        """returns str"""
        return "Подготовка пиццы " + self.dough + " " + self.sauce + " " + self.toppings

    def bake(self):
        """returns str"""
        return "Выпекаем " + self.name

    def cut(self):
        """returns str"""
        return "Нарезаем " + self.name
    def box(self):
        """returns str"""
        return "Упаковываем " + self.name


class PepperoniPizza(Pizza):
    """Pepperoni pizza"""
    def __init__(self, name, dough, sauce, toppings, price) -> None:
        super().__init__(name, dough, sauce, toppings, price)

    def __str__(self):
        return self.box()

    def prepare(self):
        print(super().prepare())
        self.bake()

    def bake(self):
        print(super().bake())
        self.cut()

    def cut(self):
        print(super().cut())
    def box(self):
        self.prepare()
        return super().box()


class BBQPizza(Pizza):
    """BBQ Pizza"""
    extra_topping = ["яйцо", "чеснок", "бекон"]
    def __init__(self, name, dough, sauce, toppings, price) -> None:
        super().__init__(name, dough, sauce, toppings, price)

    def __str__(self):
        return self.box()

    def prepare(self):
        print(super().prepare())
        self.bake()

    def bake(self):
        print(super().bake())
        self.cut()

    def cut(self):
        print(super().cut())

    def box(self):
        self.prepare()
        return super().box()

    def extra(self):
        """Add extra topping"""
        extra_choice = input("Выберите доп. начинку(яйцо, чеснок, бекон): ")
        if extra_choice.lower() in self.extra_topping:
            self.toppings = self.toppings + f" {extra_choice}"

class SeafoodPizza(Pizza):
    """Seafood Pizza"""
    def __init__(self, name, dough, sauce, toppings, price) -> None:
        super().__init__(name, dough, sauce, toppings, price)

    def __str__(self):
        return self.box()

    def prepare(self):
        print(super().prepare())
        self.bake()

    def bake(self):
        print(super().bake())
        self.cut()

    def cut(self):
        print(super().cut())

    def box(self):
        self.prepare()
        return super().box()

class Order:
    """Order"""
    pizza_order = []
    total_price = 0

    def __init__(self) -> None:
        pass

    def add_pizza(self, to_add: Pizza):
        """Adds pizza to a list"""
        self.pizza_order.append(to_add)
    def calculate_total(self):
        """Calculates total price"""
        for pizza in self.pizza_order:
            self.total_price += pizza.price
        return self.total_price

class Terminal:
    """Terminal"""
    end_state = None
    def __init__(self, pepper: PepperoniPizza,
    bbq_pizza: BBQPizza, seaf: SeafoodPizza, order: Order) -> None:
        self.pepperoni = pepper
        self.bbq_pizza = bbq_pizza
        self.seafood = seaf
        self.order = order
    def display_menu(self):
        """Displays menu"""
        print("1. Пицца Пепперони - 3500 тенге")
        print("2. Пицца Барбекю - 2500 тенге")
        print("3. Пицца Дары Моря - 4500 тенге")
        print("\nВведите номер пиццы, которую хотите добавить в заказ(0 для завершения)")

    def take_order(self):
        """Takes order"""
        pizza_dict = {1: self.pepperoni, 2: self.bbq_pizza, 3: self.seafood}
        pizza_choice = int(input("Введите номер пиццы: "))
        if pizza_choice == 0:
            self.confirm_order()
        if pizza_choice == 2:
            self.bbq_pizza.extra()
        for key, value in pizza_dict.items():
            if key == pizza_choice:
                self.order.add_pizza(value)

    def confirm_order(self):
        """Confirms order"""
        confirm_choice = input("Подтвердить заказ[y/n]: ")
        if confirm_choice.lower() == "y":
            self.take_payment()
        else:
            print("До встречи!")
            self.end_state =  "Желаете ли вы сделать новый заказ?[y/n]"

    def take_payment(self):
        """Confirms payment"""
        payment = int(self.order.calculate_total())
        pay_choice = input(f"Сумма заказа равна{payment}, подтвердите[y/n]: ")
        if pay_choice.lower() == "y":
            for good in self.order.pizza_order:
                print(good)
        else:
            print("До встречи!")
        self.end_state =  "Желаете ли вы сделать новый заказ?[y/n]"

if __name__ == "__main__":
    pepperoni = PepperoniPizza("Пепперони", "тонкое", "томатный", "пепперони", 3500)
    bbq = BBQPizza("Барбекю", "толстое", "соус барбекю", "курица", 2500)
    seafood = SeafoodPizza("Дары моря", "тонкое", "томатный", "морепродукты", 4500)
    new_order = Order()
    new_order.calculate_total()
    terminal = Terminal(pepperoni, bbq, seafood, new_order)
    while True:
        terminal.display_menu()
        terminal.take_order()
        if terminal.end_state is not None:
            final_choice = input(terminal.end_state)
            if final_choice == "y":
                terminal.end_state = None
            else:
                break
