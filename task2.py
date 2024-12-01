def task2():
    print("Задание 2: Проверка сумм трех массивов")

    # Ввод трех массивов
    arr1 = list(map(int, input("Введите элементы первого массива через пробел: ").split()))
    arr2 = list(map(int, input("Введите элементы второго массива через пробел: ").split()))
    arr3 = list(map(int, input("Введите элементы третьего массива через пробел: ").split()))

    if len(arr1) != len(arr2) or len(arr2) != len(arr3):
        print("Все массивы должны быть одинакового размера.")
        return

    results = []
    
    for a, b, c in zip(arr1, arr2, arr3):
        if a + b == c:
            results.append((a + b + c) ** min(a, b, c))
    
    print("Результаты:", results)