import doctest


class Concrete:
    def __init__(self, binder_mass: float, aggregate_mass: float, water_mass: float):
        """
        Создание и подготовка к работе объекта "Бетон"
        :param binder_mass: Масса вяжущего вещества в кг
        :param aggregate_mass: Масса заполнителей в кг
        :param water_mass: Масса воды в кг
        Примеры:
        >>> concrete = Concrete(5, 30, 2.5)  # инициализация экземпляра класса
        """
        if not isinstance(binder_mass, (int, float)):
            raise TypeError("Масса вяжущего должна быть типа int или float")
        if binder_mass <= 0:
            raise ValueError("Масса вяжущего должна быть положительным числом")
        self.binder_mass = binder_mass

        if not isinstance(aggregate_mass, (int, float)):
            raise TypeError("Масса заполнителей должна быть типа int или float")
        if aggregate_mass <= 0:
            raise ValueError("Масса заполнителей должна быть положительным числом")
        self.aggregate_mass = aggregate_mass

        if not isinstance(water_mass, (int, float)):
            raise TypeError("Масса воды должна быть типа int или float")
        if water_mass <= 0:
            raise ValueError("Масса воды должна быть положительным числом")
        self.water_mass = water_mass

    def is_get_concrete(self) -> bool:
        """
        Функция которая проверяет примняются ли все ли составляющие бетона
        Примеры:
        >>> concrete = Concrete(5, 30, 2.5)
        >>> concrete.is_get_concrete()
        """
        ...

    def remove_aggregate_from_concrete(self, estimate_concrete: float) -> None:
        """
        Функция, позволяющая уменьшить массу заполнителя в бетоне
        :param estimate_water: Масса, на которую нужно уменьшить текущую массу заполнителя
        :raise ValueError: Если извлекаемая масса заполнителя превышает текущую массу заполнителя в бетонной смеси,
        то возвращается ошибка.
        :return: Значение реально извлекаемой массы
        Примеры:
        >>> concrete = Concrete(5, 30, 2.5)
        >>> concrete.remove_aggregate_from_concrete(5)
        """
        ...

    def full_concrete_mass(self, capacity_mass: float) -> None:
        """
        Функция, подсчитывающая массу бетонной смеси с массой емкости
        :return: Масса бетонной смеси с емкостью
        Примеры:
        >>> concrete = Concrete(5, 30, 2.5)
        >>> concrete.full_concrete_mass(7)
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
# Пустая строка
