from __future__ import unicode_literals

from django.db import models


class AutoModel(models.Model):
    make = models.CharField(max_length=255, default="Audi")
    model = models.CharField(max_length=255, default="A1")
    generation = models.CharField(max_length=255, default="1")
    category = models.CharField(max_length=255, default="Sedan")
    engine = models.FloatField(default=2.0)
    engine_volume = models.IntegerField(default=1996)
    engine_power = models.IntegerField(default=220)
    maximum_torque = models.CharField(max_length=255,
                                      default="600/1500-2910")  # Нм / мин-1 600/1500-2910
    number_cylinders = models.IntegerField(default=4)
    number_valves = models.IntegerField(default=4)
    location_cylinders = models.CharField(max_length=100, default="рядная")
    fuel = models.CharField(verbose_name=u'Рекомендуемое топливо', max_length=10,
                            choices=[("АИ-92", "АИ-92"), ("АИ-95", "АИ-95"), ("АИ-98", "АИ-98"),
                                     ("Дизель", "Дизель")],
                            default="АИ-95")
    # Htcjvtylt
    # Динамические
    # характеристики
    # Время
    # разгона
    # 0 - 100
    # км / ч, с
    # 6.9
    # Максимальная
    # скорость, км / ч
    # 225
    # "Расход топлива -
    # комбинированный
    # цикл, л / 100
    # км
    # "	6.3
    # "Расход топлива -
    # городской
    # цикл, л / 100
    # км
    # "	7.3
    # "Расход топлива -
    # загородный
    # цикл, л / 100
    # км
    # "	5.7
    # Трансмиссия
    # Тип
    # коробки
    # передач
    # tiptronic
    # Количество
    # передач
    # 8
    # Ведущие
    # колеса
    # постоянный
    # полный
    # привод
    # Quattro
    # Тип
    # привода
    # Постоянный
    # полный
    # привод
    # Модель
    # Тип
    # кузова
    # Wagon
    # Число
    # мест, чел.
    # 5
    # Размеры
    # и
    # масса
    # Габаритная
    # длина, мм
    # 5052
    # Габаритная
    # ширина, мм
    # 1968
    # Габаритная
    # высота, мм
    # 1741
    # Масса
    # снаряженная, кг
    # 2055
    # Масса
    # полная, кг
    # 2750
    # Колесная
    # база, мм
    # 2994
    # Дорожный
    # просвет, мм
    # Объем
    # багажника, л
    # 770
    # Объем
    # топливного
    # бака, л
    # 75
    # Подвеска
    # Передняя
    # многорычажная
    # Задняя
    # многорычажная
    # Тормоза
    # Передние
    # дисковые
    # вентилируемые
    # Задние
    # дисковые

    def __str__(self):
        return "_".join([self.make, self.model])
