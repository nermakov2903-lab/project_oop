from abc import ABC, abstractmethod

class Iproduct(ABC):      # базовый интерфейс, для всех продуктов
    @abstractmethod
    def release(self):
        pass


class Car(Iproduct):   # конкретный продукт
    def release(self):
        print("Выпущен новый легковой автомобиль")


class Truck(Iproduct):   # конкретный продукт
    def release(self):
        print("Выпущен новый грузовой автомобиль")


class IworkShop(ABC):    # Это интерфейс для всех "мастерских"
    @abstractmethod
    def create(self) -> Iproduct:
        pass


class CarWorkShop(IworkShop):   # фабрика 1
    def create(self):
        return Car()


class TruckWorkShop(IworkShop):  # фабрика 2
    def create(self):
        return Truck()


if __name__ == "__main__":
    creator = CarWorkShop()
    car = creator.create()

    creator = TruckWorkShop()
    truck = creator.create()

    car.release()
    truck.release()



