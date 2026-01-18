class Calculator:
    """
    Класс для выполнения арифметических операций

    Methods:
        add(a, b): возвращает сумму значений a и b
    """

    @staticmethod
    def add(a, b):
        """
        Суммирует 2 числа
        Arguments:
            a (int, float): первое число
            b (int, float): второе число

        Returns:
            s (int, float): сумма чисел a и b
        """
        # примечание к конкретной строке
        s = a + b # примечание к конкретной строке
        return s


if __name__ == '__main__':
    print(Calculator.__doc__)
    print(Calculator.add.__doc__)
