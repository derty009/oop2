from attributes import Price
from factories import (
    BreadFactory,
    JacketFactory,
    LaptopFactory,
    MilkFactory,
    SmartphoneFactory,
    TShirtFactory,
)
from warehouse import Warehouse


def print_warehouse(warehouse):
    print(warehouse)
    for product in warehouse:
        print("  ", product)


def create_filled_warehouse():
    warehouse = Warehouse(10)
    warehouse.add_product(SmartphoneFactory().create_product("Galaxy S24", 80000, 5, 0.17))
    warehouse.add_product(LaptopFactory().create_product("ThinkPad X1", 150000, 3, 1.1))
    warehouse.add_product(TShirtFactory().create_product("Футболка белая", 1500, 40, 0.2))
    warehouse.add_product(JacketFactory().create_product("Куртка зимняя", 12000, 7, 1.4))
    warehouse.add_product(MilkFactory().create_product("Молоко", 90, 100, 1.0))
    warehouse.add_product(BreadFactory().create_product("Хлеб", 90, 50, 0.4))
    return warehouse


def demo_create():
    print()
    print("--- Сценарий 1: создание склада, фабрики, итератор ---")
    warehouse = create_filled_warehouse()
    print_warehouse(warehouse)

    print("Уменьшаем остаток всех товаров на 1 через итератор:")
    for product in warehouse:
        product.change_quantity(-1)
    print_warehouse(warehouse)

    print("Пробуем превысить лимит склада:")
    small = Warehouse(1)
    small.add_product(MilkFactory().create_product("Молоко", 90, 1, 1.0))
    try:
        small.add_product(BreadFactory().create_product("Хлеб", 50, 1, 0.4))
    except ValueError as error:
        print("Ошибка:", error)


def demo_copy():
    print()
    print("--- Сценарий 2: копирование склада ---")
    original = create_filled_warehouse()
    duplicate = original.make_copy()

    for product in duplicate:
        product.change_quantity(-1)
        product.set_price(Price(1))
    duplicate.remove_by_index(0)

    print("Оригинал (не изменился):")
    print_warehouse(original)
    print("Копия (изменена):")
    print_warehouse(duplicate)


def demo_move():
    print("--- Сценарий 3: перемещение склада ---")
    first = create_filled_warehouse()
    first_product = first.products[0]

    second = Warehouse(1)
    second.move_from(first)

    print("Старый склад:", first)
    print("Новый склад:", second)
    print("Это тот же объект товара, копии нет:", second.products[0] is first_product)


def demo_search():
    print("--- Сценарий 4: поиск и удаление ---")
    warehouse = create_filled_warehouse()
    first_id = warehouse.products[0].id

    print("Поиск по id", first_id, ":", warehouse.find_by_id(first_id))
    print("Поиск по несуществующему id:", warehouse.find_by_id(-1))

    print("Поиск по категории food:")
    for product in warehouse.find_by_category("food"):
        print("  ", product)

    print("Поиск по цене 90:")
    for product in warehouse.find_by_price(Price(90)):
        print("  ", product)

    print("Удален по id:", warehouse.remove_by_id(first_id))
    print("Удален по индексу 0:", warehouse.remove_by_index(0))
    print_warehouse(warehouse)


def demo_transfer():
    print("--- Сценарий 5: перемещение товара между складами ---")
    main_warehouse = create_filled_warehouse()
    branch = Warehouse(2)

    phone = main_warehouse.find_by_category("electronics")[0]
    phone.transfer_to(branch)
    phone.change_quantity(-2)
    phone.set_price(Price(75000))

    print("Основной склад:")
    print_warehouse(main_warehouse)
    print("Филиал:")
    print_warehouse(branch)

    print("Пробуем сделать остаток отрицательным:")
    try:
        phone.change_quantity(-100)
    except ValueError as error:
        print("Ошибка:", error)

    print("Пробуем создать отрицательную цену:")
    try:
        Price(-1)
    except ValueError as error:
        print("Ошибка:", error)


def main():
    while True:
        print("===== МЕНЮ =====")
        print("1 - создание склада, фабрики, итератор")
        print("2 - копирование склада")
        print("3 - перемещение склада")
        print("4 - поиск и удаление")
        print("5 - перемещение товара между складами")
        print("0 - выход")

        try:
            choice = input("Выбор: ")
        except EOFError:
            break

        if choice == "1":
            demo_create()
        elif choice == "2":
            demo_copy()
        elif choice == "3":
            demo_move()
        elif choice == "4":
            demo_search()
        elif choice == "5":
            demo_transfer()
        elif choice == "0":
            break
        else:
            print("Нет такого пункта")


if __name__ == "__main__":
    main()

