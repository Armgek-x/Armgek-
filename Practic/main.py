import libriry

print("Добро пожаловать!")
print("Данный код является проверяющим кодом для моей библеотеки,\nзанимающаяся тем, что помогает переводить часы в минуты, минуты в секунды,\nа также биты в байты, килобайты и тп")
print("Введите: task1 - для перевода времени")
print("Введите: task2 - для перевода размеров файла")

taskEditor = (input("Введите задание: "))

def task1():
    print("\n--- Перевод времени ---")
    val = float(input("Введите число: "))
    print("1. Часы в минуты")
    print("2. Минуты в секунды")
    choice = input("Выберите направление (1 или 2): ")
    
    if choice == "1":
        res = libriry.convert_time(val, "hours_to_mins")
        print(f"Результат: {res} минут")
    elif choice == "2":
        res = libriry.convert_time(val, "mins_to_secs")
        print(f"Результат: {res} секунд")
    else:
        print("Неверный выбор направления.")

def task2():
    print("\n--- Перевод размеров файла ---")
    val = float(input("Введите значение: "))
    
    print("Что во что переводим?")
    print("1. Из байтов в килобайты (Кб)")
    print("2. Из килобайтов (Кб) в мегабайты (Мб)")
    print("3. Из мегабайтов (Мб) в гигабайты (Гб)")
    print("4. Из гигабайтов (Гб) в мегабайты (Мб)")
    print("5. Из мегабайтов (Мб) в килобайты (Кб)")
    print("6. Из килобайтов (Кб) в байты")
    
    choice = input("Выберите вариант (1-6): ")
    
    if choice == "1":
        res = libriry.convert_size(val, "to_larger", "bytes", "kb")
        print(f"Результат: {res} Кб")
    elif choice == "2":
        res = libriry.convert_size(val, "to_larger", "kb", "mb")
        print(f"Результат: {res} Мб")
    elif choice == "3":
        res = libriry.convert_size(val, "to_larger", "mb", "gb")
        print(f"Результат: {res} Гб")
    elif choice == "4":
        res = libriry.convert_size(val, "to_smaller", "gb", "mb")
        print(f"Результат: {res} Мб")
    elif choice == "5":
        res = libriry.convert_size(val, "to_smaller", "mb", "kb")
        print(f"Результат: {res} Кб")
    elif choice == "6":
        res = libriry.convert_size(val, "to_smaller", "kb", "bytes")
        print(f"Результат: {res} байт")
    else:
        print("Слишком сложный выбор для простого меню!")

status = True
while status:
    if taskEditor == "task1":
        task1() 
        if (input("Еще раз?") != "Да"):
            status = False  
    elif taskEditor == "task2":
        task2()
        if (input("Еще раз?") != "Да"):
            status = False
    else:
        print("Не удалось понять задачу")
        if (input("Еще раз?") != "Да"):
            status = False