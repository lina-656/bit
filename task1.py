def task1():
    print("Задание 1: Сумма двух массивов")

    # Ввод первого массива
    arr1 = list(map(int, input("Введите элементы первого массива через пробел: ").split()))
    # Ввод второго массива
    arr2 = list(map(int, input("Введите элементы второго массива через пробел: ").split()))

    if len(arr1) != len(arr2):
        print("Массивы должны быть одинакового размера.")
        return

    # Сортировка массивов
    arr1.sort(reverse=True)  # Убывание
    arr2.sort()               # Возрастание

    # Вычисление суммы
    result = []
    for a, b in zip(arr1, arr2):
        if a == b:
            result.append(0)
        else:
            result.append(a + b)

    # Сортировка результата
    result.sort()
    print("Результат:", result)