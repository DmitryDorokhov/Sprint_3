def validate_fuel_consumption(method):
    ""    Декоратор для проверки условий перед расчётом расхода топлива.
    Проверяет, что время или расстояние неотрицательны и достаточно топлива.
    """
    def wrapper(self, value):
        # вызов метода: method(self, value)
        if value < 0:
            print('"Ошибка: значение не может быть отрицательным."')
            return None

        # 2. Вызов исходного метода для получения чистого расхода
        consumption = method(self, value)        
        # Если метод вернул None (например, ошибка деления или внутренняя проверка), выходим
        if consumption is None:
            return None
            
        # 3. Проверка на достаточное количество топлива
        if consumption > self._current_fuel_level:
            print(f"Ошибка: недостаточно топлива для поездки. Нужно {consumption:.2f} л, в наличии {self._current_fuel_level:.2f} л.")
            return None
            
        # 4. Списание топлива и возврат значения
        self._current_fuel_level -= consumption
        return consumption


    return wrapper


class Vehicle:
    """
    Базовый класс для транспортных средств.
    """
    def __init__(self, name: str, fuel_tank_capacity: float):
        self._name = name
        self._fuel_tank_capacity = fuel_tank_capacity
        # При создании объекта бак полностью заправлен
        self._current_fuel_level = fuel_tank_capacity


    def refuel(self, amount: float):
        """
        Заправка транспортного средства.
        """
        if amount <= 0:
            print('"Ошибка: количество топлива должно быть положительным."')
            return
        
        free_space = self._fuel_tank_capacity - self._current_fuel_level
        
        if amount > free_space:
            print('"Ошибка: превышение вместимости топливного бака."')
            return
        else:
            self._current_fuel_level += amount
            print(f'"Заправлено {amount} л. Текущий уровень: {self._current_fuel_level} л."')



    def display_info(self):
        """
        Отображает основную информацию о транспортном средстве.
        """
        print(f'Название: {self._name}, '
                f'Вместимость бака: {self._fuel_tank_capacity} л, '
                f'Текущий уровень топлива: {self._current_fuel_level} л.')


class Car(Vehicle):
    """
    Класс для представления автомобиля.
    Наследует от Vehicle.
    """
    def __init__(self, name: str, fuel_tank_capacity: float, fuel_consumption_per_100km: float):
        super().__init__(name, fuel_tank_capacity)
        self._fuel_consumption_per_100km = fuel_consumption_per_100km
    
    @validate_fuel_consumption
    def calculate_fuel_consumption(self, distance:float) -> float:
        calculated_consumption = (distance / 100) * self._fuel_consumption_per_100km
        print(f'Расход на {distance} км: {calculated_consumption:.2f} л.')
        return calculated_consumption           

class Airplane(Vehicle):
    """
    Класс для представления самолёта.
    Наследует от Vehicle.
    """
    def __init__(self, name: str, fuel_tank_capacity: float, fuel_consumption_per_hour: float):
        super().__init__(name, fuel_tank_capacity)
        self._fuel_consumption_per_hour = fuel_consumption_per_hour

    @validate_fuel_consumption
    def calculate_fuel_consumption(self, flight_time:float) -> float:
        calculated_consumption = flight_time * self._fuel_consumption_per_hour
        print(f'Расход за {flight_time} ч: {calculated_consumption} л.')
        return calculated_consumption 


class Boat(Vehicle):
    """
    Класс для представления катера.
    Наследует от Vehicle.
    """
    def __init__(self, name: str, fuel_tank_capacity: float, fuel_consumption_per_hour: float):
        super().__init__(name, fuel_tank_capacity)
        self._fuel_consumption_per_hour = fuel_consumption_per_hour

    @validate_fuel_consumption
    def calculate_fuel_consumption(self, travel_time:float) -> float:
        calculated_consumption = travel_time * self._fuel_consumption_per_hour
        print(f'Расход за {travel_time} ч: {calculated_consumption} л.')
        return calculated_consumption 


# Создание объектов
car = Car("Toyota Camry", -60, 8)
airplane = Airplane("Boeing 737", 20000, 2500)
boat = Boat("Sea Ray", 150, 30)

# Отображение информации
car.display_info() # Название: Toyota Camry, Вместимость бака: 60 л, Текущий уровень топлива: 60 л.
airplane.display_info() # Название: Boeing 737, Вместимость бака: 20000 л, Текущий уровень топлива: 20000 л.
boat.display_info() # Название: Sea Ray, Вместимость бака: 150 л, Текущий уровень топлива: 150 л.

# Заправка транспортных средств
car.refuel(30) # Ошибка: превышение вместимости топливного бака.
airplane.refuel(10000) # Ошибка: превышение вместимости топливного бака.
boat.refuel(80) # Ошибка: превышение вместимости топливного бака.

# Расчёт расхода топлива
car.calculate_fuel_consumption(150) # Расход на 150 км: 12.00 л.
airplane.calculate_fuel_consumption(3) # Расход за 3 ч: 7500.00 л.
boat.calculate_fuel_consumption(2) # Расход за 2 ч: 60.00 л .
