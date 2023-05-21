from abc import ABC, abstractmethod


class House(ABC):
    @abstractmethod
    def get_house_type(self):
        '''получаем тип дома'''

    @abstractmethod
    def get_floor_count(self):
        '''получаем количество этажей'''


class WoodenHouse(House):
    def __init__(self, floor):
        self.floor = floor

    def get_house_type(self):
        return "Деревянный дом"

    def get_floor_count(self):
        return self.floor


class BrickHouse(House):
    def __init__(self, floor):
        self.floor = floor

    def get_house_type(self):
        return "Кирпичный дом"

    def get_floor_count(self):
        return self.floor


class HouseFactory:
    @staticmethod
    def create_house(house_type, floor):
        if house_type == "Wooden":
            return WoodenHouse(floor)
        elif house_type == "Brick":
            return BrickHouse(floor)
        else:
            raise ValueError("Дом должен быть либо кирпичным, либо деревянным")


def client_code(factory, house_type, floor):
    house = factory.create_house(house_type, floor)
    print("Тип дома:", house.get_house_type())
    print("Количество этажей:", house.get_floor_count())


if __name__ == '__main__':
    wooden_house_factory = HouseFactory()
    brick_house_factory = HouseFactory()

    client_code(wooden_house_factory, 'Wooden', 1)
    client_code(brick_house_factory, 'Brick', 2)
