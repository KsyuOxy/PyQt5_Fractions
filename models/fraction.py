"""
Реализовать:
- перегрузĸи операторов арифметичесĸих действий c дробями в ĸлассе Fraction;
- операции соĸращения дробей по алгоритму Эвĸлида.
"""


class Fraction(object):
    def __init__(self, entier: int, numerator: int, denominator: int):
        self._numerator = numerator  # -> числитель
        self._denominator = denominator  # -> знаменатель
        self._entier = entier  # -> целая часть

    def __str__(self):  # -> переопределяет метод str
        if self._entier != 0 and self._numerator == self._denominator:
            return f'{self._entier}'  # -> выводит только целую часть, если числитель и знаменатель равны

        elif self._entier == 0 and self._numerator == 0 and self._denominator == 0:
            return '0'  # -> выводит 0, если все аргументы нулевые

        elif self._entier == 0:
            return f'{self._numerator}/{self._denominator}'  # -> выводит только дробную часть, если целая часть нулевая

        else:
            if self._entier < 0:  # -> выводит отрицательный знак только у целой части
                return f'{self._entier} {abs(self._numerator)}/{abs(self._denominator)}'
            else:
                return f'{self._entier} {self._numerator}/{self._denominator}'

    def get_numerator(self):
        return self._numerator

    def get_denominator(self):
        return self._denominator

    def get_entier(self):
        return self._entier

    def common_fraction(self):
        """
        Преобразовывает в обыкновенную дробь
        :return: Fraction
        """
        if self._entier != 0 and self._numerator == 0 and self._denominator == 0:  # -> преобразов. целое число в дробь
            numerator = self._entier
            denominator = 1
            entier = 0
            return Fraction(entier, numerator, denominator)

        elif self._entier != 0 and self._numerator == 0 or self._denominator == 0:
            return None

        elif self._entier != 0:
            entier_sign = int(self._entier / abs(self._entier))
            numerator = (self._numerator + abs(self._entier) * self._denominator) * entier_sign
            entier = 0
            return Fraction(entier, numerator, self._denominator)

        else:
            return Fraction(self._entier, self._numerator, self._denominator)

    def __add__(self, other):
        """
        Складывает дроби
        :param other: Fraction
        :return: Fraction
        """
        self_fraction = self.common_fraction()  # -> перевод в обыкновенную дробь
        other_fraction = other.common_fraction()  # -> перевод в обыкновенную дробь

        numerator1 = self_fraction.get_numerator()  # -> получает числитель первого числа
        numerator2 = other_fraction.get_numerator()  # -> получает числитель второго числа

        denominator_1 = self_fraction.get_denominator()  # -> получает знаменатель первого числа
        denominator_2 = other_fraction.get_denominator()  # -> получает знаменатель второго числа

        if denominator_1 == denominator_2:  # -> сложение дробей с одинаковыми знаменателями -----------------------
            numerator = numerator1 + numerator2  # -> числитель
            denominator = denominator_1  # -> знаменатель
            entier = 0  # -> целая часть

            return Fraction(entier, numerator, denominator).entier()

        else:
            lowest_common_denominator = 0  # -> наименьший общий знаменатель

            if denominator_1 > denominator_2:  # -> решение, если знаменатель первого числа больше второго ---------
                for n in range(1, abs(denominator_2) + 1):
                    if (denominator_1 * n) % abs(denominator_2) == 0:
                        lowest_common_denominator += denominator_1 * n
                        numerator1 *= n
                        numerator2 *= int((denominator_1 * n) / denominator_2)
                        break
                denominator = lowest_common_denominator  # -> знаменатель
                numerator = numerator1 + numerator2  # -> числитель
                entier = 0  # -> целая часть

                return Fraction(entier, numerator, denominator).entier()

            elif denominator_2 > denominator_1:  # -> решение, если знаменатель второго числа больше первого -------
                for n in range(1, abs(denominator_1) + 1):
                    if (denominator_2 * n) % abs(denominator_1) == 0:
                        lowest_common_denominator += denominator_2 * n
                        numerator2 *= n
                        numerator1 *= int((denominator_2 * n) / denominator_1)
                        break
                denominator = lowest_common_denominator  # -> знаменатель
                numerator = numerator1 + numerator2  # -> числитель
                entier = 0  # -> целая часть

                return Fraction(entier, numerator, denominator).entier()

    def __sub__(self, other):
        """
        Вычитает дроби
        :param other: Fraction
        :return: Fraction
        """
        self_fraction = self.common_fraction()  # -> перевод в обыкновенную дробь
        other_fraction = other.common_fraction()  # -> перевод в обыкновенную дробь

        numerator1 = self_fraction.get_numerator()  # -> получает числитель первого числа
        numerator2 = other_fraction.get_numerator()  # -> получает числитель второго числа

        denominator_1 = self_fraction.get_denominator()  # -> получает знаменатель первого числа
        denominator_2 = other_fraction.get_denominator()  # -> получает знаменатель второго числа

        if denominator_1 == denominator_2:  # -> вычитание дробей с одинаковыми знаменателями -----------------------
            numerator = numerator1 - numerator2  # -> числитель

            if numerator == 0:  # -> Если числитель равен нулю, возвращает нули
                return Fraction(0, 0, 0)

            denominator = denominator_1  # -> знаменатель
            entier = 0  # -> целая часть

            return Fraction(entier, numerator, denominator).entier()
        else:
            lowest_common_denominator = 0  # -> наименьший общий знаменатель

            if denominator_1 > denominator_2:  # -> решение, если знаменатель первого числа больше второго ---------
                for n in range(1, abs(denominator_2) + 1):
                    if (denominator_1 * n) % abs(denominator_2) == 0:
                        lowest_common_denominator += denominator_1 * n
                        numerator1 *= n
                        numerator2 *= int((denominator_1 * n) / denominator_2)
                        break
                denominator = lowest_common_denominator  # -> знаменатель
                numerator = numerator1 - numerator2  # -> числитель
                entier = 0  # -> целая часть

                return Fraction(entier, numerator, denominator).entier()

            elif denominator_2 > denominator_1:  # -> решение, если знаменатель второго числа больше первого -------
                for n in range(1, abs(denominator_1) + 1):
                    if (denominator_2 * n) % abs(denominator_1) == 0:
                        lowest_common_denominator += denominator_2 * n
                        numerator2 *= n
                        numerator1 *= int((denominator_2 * n) / denominator_1)
                        break
                denominator = lowest_common_denominator  # -> знаменатель
                numerator = numerator1 - numerator2  # -> числитель
                entier = 0  # -> целая часть

                return Fraction(entier, numerator, denominator).entier()

    def __mul__(self, other):
        """
        Умножает дроби
        :param other: Fraction
        :return: Fraction
        """
        self_fraction = self.common_fraction()  # -> перевод в обыкновенную дробь
        other_fraction = other.common_fraction()  # -> перевод в обыкновенную дробь

        numerator_1 = self_fraction.get_numerator()  # -> получает числитель первого числа
        numerator_2 = other_fraction.get_numerator()  # -> получает числитель второго числа

        denominator_1 = self_fraction.get_denominator()  # -> получает знаменатель первого числа
        denominator_2 = other_fraction.get_denominator()  # -> получает знаменатель второго числа

        numerator = numerator_1 * numerator_2  # -> числитель
        denominator = denominator_1 * denominator_2  # -> знаменатель
        entier = 0  # -> целая часть

        return Fraction(entier, numerator, denominator).entier()

    def __truediv__(self, other):
        """
        Делит дроби
        :param other: Fraction
        :return: Fraction
        """
        self_fraction = self.common_fraction()  # -> перевод в обыкновенную дробь
        other_fraction = other.common_fraction()  # -> перевод в обыкновенную дробь

        numerator_1 = self_fraction.get_numerator()  # -> получает числитель первого числа
        numerator_2 = other_fraction.get_numerator()  # -> получает числитель второго числа

        denominator_1 = self_fraction.get_denominator()  # -> получает знаменатель первого числа
        denominator_2 = other_fraction.get_denominator()  # -> получает знаменатель второго числа

        numerator = numerator_1 * denominator_2
        denominator = denominator_1 * numerator_2
        entier = 0  # -> целая часть

        return Fraction(entier, numerator, denominator).entier()

    def entier(self):
        """
        Выделяет целую часть из дроби
        :return: Fraction
        """
        if self._entier != 0:  # -> если дробь смешанная и целая часть уже присутствует
            entier_sign = int(self._entier / abs(self._entier))  # -> сохраняет знак целого значения смешанной дроби

            # -> выделяет из дробной части целое и добавляет к уже существующей целой части
            entier = (abs(self._entier) + (self._numerator // self._denominator)) * entier_sign

            numerator = self._numerator - (self._numerator // self._denominator) * self._denominator  # -> нов.числитель

            if numerator == 0:  # -> если числитель '0', значит дробь делится без остатка и дробная часть не нужна
                denominator = 0
            else:
                denominator = self._denominator
            return Fraction(entier, numerator, denominator)

        elif self._entier == 0:
            if self._numerator == 0:
                return Fraction(0, 0, 0)
            numerator_sign = int(self._numerator / abs(self._numerator))  # -> знак числителя
            denominator_sign = int(self._denominator / abs(self._denominator))  # -> знак знаменателя

            # -> вычисление целой части
            entier = int(abs(self._numerator) // abs(self._denominator)) * numerator_sign * denominator_sign

            numerator = self._numerator - entier * self._denominator  # -> вычисление числителя

            if numerator == 0:  # -> если числитель '0', значит дробь делится без остатка и дробная часть не нужна
                denominator = 0
            else:
                denominator = self._denominator
            return Fraction(entier, numerator, denominator)

    def reduce_fraction(self):
        """
        Сокращает дробь (алгоритм Евклида)
        :return: Fraction
        """
        number_1 = self._numerator  # -> будет хранить изменяющееся значение
        number_2 = self._denominator  # -> будет хранить изменяющееся значение
        numerator = self._numerator  # -> числитель
        denominator = self._denominator  # -> знаменатель
        entier = self._entier  # -> целая часть

        def reduce() -> Fraction:  # -> рекурсивная функция сокращает дробь
            nonlocal number_1, number_2, entier, numerator, denominator

            if number_1 > number_2:
                if number_1 % number_2 == 0:  # -> если деление без остатка, значит число 2 является НОД
                    numerator = int(self._numerator / abs(number_2))
                    denominator = int(self._denominator / abs(number_2))
                    entier = self._entier

                    return Fraction(entier, numerator, denominator)

                else:
                    number_1 = number_1 % number_2  # -> присв. переменной большего числа остаток от деления на меньшее

                    if number_2 % number_1 == 0:  # -> если деление без остатка, значит число 1 является НОД
                        numerator = int(self._numerator / abs(number_1))
                        denominator = int(self._denominator / abs(number_1))
                        entier = self._entier
                        return Fraction(entier, numerator, denominator)

                    else:
                        number_2 = number_2 % number_1  # -> присв. переменной больш.числа остаток от деления на меньшее
                        reduce()  # -> рекурсия

                return Fraction(entier, numerator, denominator)

            elif number_2 > number_1:
                if number_2 % number_1 == 0:  # -> если деление без остатка, значит число 1 является НОД
                    numerator = int(self._numerator / abs(number_1))
                    denominator = int(self._denominator / abs(number_1))
                    entier = self._entier

                    return Fraction(entier, numerator, denominator)
                else:
                    number_2 = number_2 % number_1  # -> присв. переменной большего числа остаток от деления на меньшее

                    if number_1 % number_2 == 0:  # -> если деление без остатка, значит число 2 является НОД
                        numerator = int(self._numerator / abs(number_2))
                        denominator = int(self._denominator / abs(number_2))
                        entier = self._entier
                        return Fraction(entier, numerator, denominator)
                    else:
                        number_1 = number_1 % number_2  # -> присв. переменной больш.числа остаток от деления на меньшее
                        reduce()  # -> рекурсия

                return Fraction(entier, numerator, denominator)

        return reduce()


a = Fraction(0, 272, 136)
b = Fraction(0, 3, 1)
c = Fraction(3, 2, 4)

print(a.reduce_fraction())
