from abc import ABC, abstractmethod

from attributes import Price, Quantity, Weight


class Product(ABC):
    next_id = 1

    def __init__(self, name, price, quantity, weight, category, product_id=None):
        if product_id is None:
            product_id = Product.next_id
        if product_id >= Product.next_id:
            Product.next_id = product_id + 1

        self.id = product_id
        self.name = name
        self.price = Price(price)
        self.quantity = Quantity(quantity)
        self.weight = Weight(weight)
        self.category = category
        self.warehouse = None

    @abstractmethod
    def clone(self):
        pass

    def change_quantity(self, delta):
        self.quantity.change(delta)

    def set_price(self, new_price):
        self.price = Price(new_price.get_value())

    def transfer_to(self, other):
        if self.warehouse is None:
            raise ValueError("Товар не лежит на складе")
        if other is self.warehouse:
            raise ValueError("Товар уже на этом складе")
        # проверяем заранее, чтобы при ошибке товар не пропал с первого склада
        if other.is_full():
            raise ValueError("Склад назначения заполнен")
        if other.find_by_id(self.id) is not None:
            raise ValueError("На складе назначения уже есть товар с таким id")

        self.warehouse.remove_by_id(self.id)
        other.add_product(self)

    def __str__(self):
        return (
            type(self).__name__ + " #" + str(self.id) + " " + self.name
            + " [" + self.category + "]"
            + " цена=" + str(self.price)
            + " остаток=" + str(self.quantity)
            + " вес=" + str(self.weight)
        )


class Electronics(Product):
    def __init__(self, name, price, quantity, weight, product_id=None):
        super().__init__(name, price, quantity, weight, "electronics", product_id)


class Clothing(Product):
    def __init__(self, name, price, quantity, weight, product_id=None):
        super().__init__(name, price, quantity, weight, "clothing", product_id)


class Food(Product):
    def __init__(self, name, price, quantity, weight, product_id=None):
        super().__init__(name, price, quantity, weight, "food", product_id)


class Smartphone(Electronics):
    def clone(self):
        return Smartphone(self.name, self.price.get_value(), self.quantity.get_value(),
                          self.weight.get_value(), self.id)


class Laptop(Electronics):
    def clone(self):
        return Laptop(self.name, self.price.get_value(), self.quantity.get_value(),
                      self.weight.get_value(), self.id)


class TShirt(Clothing):
    def clone(self):
        return TShirt(self.name, self.price.get_value(), self.quantity.get_value(),
                      self.weight.get_value(), self.id)


class Jacket(Clothing):
    def clone(self):
        return Jacket(self.name, self.price.get_value(), self.quantity.get_value(),
                      self.weight.get_value(), self.id)


class Milk(Food):
    def clone(self):
        return Milk(self.name, self.price.get_value(), self.quantity.get_value(),
                    self.weight.get_value(), self.id)


class Bread(Food):
    def clone(self):
        return Bread(self.name, self.price.get_value(), self.quantity.get_value(),
                     self.weight.get_value(), self.id)
