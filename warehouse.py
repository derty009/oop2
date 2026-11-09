import copy


class WarehouseIterator:
    def __init__(self, products):
        # берем копию списка, чтобы в цикле можно было перемещать товары
        # и не пропускать из-за этого следующий
        self.products = list(products)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.products):
            raise StopIteration
        product = self.products[self.index]
        self.index += 1
        return product


class Warehouse:
    def __init__(self, max_size):
        if max_size <= 0:
            raise ValueError("Размер склада должен быть больше нуля")
        self.max_size = max_size
        self.products = []

    def size(self):
        return len(self.products)

    def is_full(self):
        return len(self.products) >= self.max_size

    def add_product(self, product):
        if self.is_full():
            raise ValueError("Склад заполнен")
        if product.warehouse is not None:
            raise ValueError("Товар уже лежит на складе, используйте transfer_to")
        if self.find_by_id(product.id) is not None:
            raise ValueError("Товар с таким id уже есть на складе")
        product.warehouse = self
        self.products.append(product)

    def remove_by_id(self, product_id):
        for i in range(len(self.products)):
            if self.products[i].id == product_id:
                return self.remove_by_index(i)
        raise ValueError("Товар с id " + str(product_id) + " не найден")

    def remove_by_index(self, index):
        if index < 0 or index >= len(self.products):
            raise IndexError("Неверный индекс " + str(index))
        product = self.products.pop(index)
        product.warehouse = None
        return product

    def find_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def find_by_category(self, category):
        result = []
        for product in self.products:
            if product.category == category:
                result.append(product)
        return result

    def find_by_price(self, price):
        result = []
        for product in self.products:
            if product.price.get_value() == price.get_value():
                result.append(product)
        return result

    def make_copy(self):
        return copy.deepcopy(self)

    def move_from(self, other):
        if other is self:
            return
        for product in self.products:
            product.warehouse = None
        self.products = other.products
        self.max_size = other.max_size
        other.products = []
        for product in self.products:
            product.warehouse = self

    def __iter__(self):
        return WarehouseIterator(self.products)

    def __len__(self):
        return len(self.products)

    def __str__(self):
        return "Склад: " + str(len(self.products)) + " из " + str(self.max_size) + " товаров"
