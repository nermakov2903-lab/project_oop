# Продукты
def create_car():
    """Создание легкового автомобиля"""
    def release():
        print("Выпущен новый легковой автомобиль")
    return {"type": "car", "release": release}


def create_truck():
    """Создание грузового автомобиля"""
    def release():
        print("Выпущен новый грузовой автомобиль")
    return {"type": "truck", "release": release}


# Фабричный метод
def vehicle_factory(vehicle_type: str):
    """Фабрика для создания автомобилей"""
    factories = {
        "car": create_car,
        "truck": create_truck
    }

    creator = factories.get(vehicle_type)
    return creator()  # возвращает словарь с функцией release



if __name__ == "__main__":
    # создаем легковую машину
    car = vehicle_factory("car")
    car["release"]()

    # создаем грузовик
    truck = vehicle_factory("truck")
    truck["release"]()
