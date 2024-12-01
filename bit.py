from task1 import task1
from task2 import task2
from task3 import task3

def print_menu():
    print("\nМеню:")
    print("1. Задание 1")
    print("2. Задание 2")
    print("3. Задание 3")
    print("4. Завершение работы программы")

def main():
    while True:
        print_menu()
        choice = input("Выберите пункт меню: ")

        if choice == '1':
            task1()
        elif choice == '2':
            task2()
        elif choice == '3':
            task3()
        elif choice == '4':
            print("Завершение работы программы.")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()