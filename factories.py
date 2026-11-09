from abc import ABC, abstractmethod

from products import Bread, Jacket, Laptop, Milk, Smartphone, TShirt


class ProductFactory(ABC):
    @abstractmethod
    def create_product(self, name, price, quantity, weight, product_id=None):
        pass


class SmartphoneFactory(ProductFactory):
    def create_product(self, name, price, quantity, weight, product_id=None):
        return Smartphone(name, price, quantity, weight, product_id)


class LaptopFactory(ProductFactory):
    def create_product(self, name, price, quantity, weight, product_id=None):
        return Laptop(name, price, quantity, weight, product_id)


class TShirtFactory(ProductFactory):
    def create_product(self, name, price, quantity, weight, product_id=None):
        return TShirt(name, price, quantity, weight, product_id)


class JacketFactory(ProductFactory):
    def create_product(self, name, price, quantity, weight, product_id=None):
        return Jacket(name, price, quantity, weight, product_id)


class MilkFactory(ProductFactory):
    def create_product(self, name, price, quantity, weight, product_id=None):
        return Milk(name, price, quantity, weight, product_id)


class BreadFactory(ProductFactory):
    def create_product(self, name, price, quantity, weight, product_id=None):
        return Bread(name, price, quantity, weight, product_id)
