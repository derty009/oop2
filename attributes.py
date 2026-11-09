class Price:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError("Цена не может быть отрицательной")
        self._value = new_value

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def __str__(self):
        return str(self._value)


class Quantity:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError("Остаток не может быть отрицательным")
        self._value = new_value

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def change(self, delta):
        self.value = self._value + delta

    def __str__(self):
        return str(self._value)


class Weight:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError("Вес не может быть отрицательным")
        self._value = new_value

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def __str__(self):
        return str(self._value)
