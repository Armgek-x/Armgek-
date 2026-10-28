shop_libriry = {
"mouse": {

    "id" : 1,
    "name" : "Мышь",
    "category" : "Внешние устройства",
    "price" : 700,
    "quantity" : 7

},

"keyboard": {

    "id" : 2,
    "name" : "Клавиатура",
    "category" : "Внешние устройства",
    "price" : 800,
    "quantity" : 8

},

"monitor": {

    "id" : 3,
    "name" : "Монитор",
    "category" : "Внешние устройства",
    "price" : 3500,
    "quantity" : 6

},

"headphones": {

    "id" : 4,
    "name" : "Наушники",
    "category" : "Звук",
    "price" : 2500,
    "quantity" : 2

},

"web_camera": {

    "id" : 5,
    "name" : "Веб-камера",
    "category" : "Дополнительные устройства",
    "price" : 800,
    "quantity" : 0

},   

"microphone": {

    "id" : 6,
    "name" : "Микрофон",
    "category" : "Дополнительные устройства",
    "price" : 500,
    "quantity" : 4

},

"speakers": {

    "id" : 7,
    "name" : "Колонки",
    "category" : "Звук",
    "price" : 800,
    "quantity" : 3

},

"usb_flash": {

    "id" : 8,
    "name" : "USB-флешка",
    "category" : "Файловый носитель",
    "price" : 500,
    "quantity" : 0

}
}

print("Добро пожаловать!")
print("Для вывода интересующих вас вопросов используйте следующие команды")
print("Введите: task1 - для вывода ассортимента")
print("Введите: task2 - для поиск товаров")
print("Введите: task3 - для Фильтрация по категории")
print("Введите: task4 - для работы с остатками на складе")
print("Введите: task5 - для изменение количества товара")
print("Введите: task6 - для продажи товара")
print("Введите: task7 - для статистики магазина")
print("Введите: task8 - для сортировка товаров")
print("Введите: task9 - для меню программы")

taskEditor = (input("Введите задание: "))

# Задание 1 
def task1():
    print("Вот наш полный ассортимент: ", shop_libriry)
    print("Общая стоимость всех товаров на складе: ", (shop_libriry["mouse"]["price"] * shop_libriry["mouse"]["quantity"])
            + (shop_libriry["keyboard"]["price"] * shop_libriry["keyboard"]["quantity"]) 
            + (shop_libriry["monitor"]["price"] * shop_libriry["monitor"]["quantity"]) 
            + (shop_libriry["headphones"]["price"] * shop_libriry["headphones"]["quantity"]) 
            + (shop_libriry["web_camera"]["price"] * shop_libriry["web_camera"]["quantity"]) 
            + (shop_libriry["microphone"]["price"] * shop_libriry["microphone"]["quantity"]) 
            + (shop_libriry["speakers"]["price"] * shop_libriry["speakers"]["quantity"]) 
            + (shop_libriry["usb_flash"]["price"] * shop_libriry["usb_flash"]["quantity"]))


# Задание 2 
def task2():
    search = str(input("Введите товар: "))
    for key, value in shop_libriry.items():
        if search == shop_libriry["mouse"]["name"]:  
            print(shop_libriry["mouse"]["name"])
            break
        elif search == shop_libriry["headphones"]["name"]:
            print(shop_libriry["headphones"]["name"])
            break
        elif search == shop_libriry["keyboard"]["name"]: 
            print(shop_libriry["keyboard"]["name"])
            break
        elif search == shop_libriry["microphone"]["name"]: 
            print(shop_libriry["microphone"]["name"])
            break
        elif search == shop_libriry["monitor"]["name"]: 
            print(shop_libriry["monitor"]["name"])
            break
        elif search == shop_libriry["speakers"]["name"]:  
            print(shop_libriry["speakers"]["name"])
            break
        elif search == shop_libriry["usb_flash"]["name"]: 
            print(shop_libriry["usb_flash"]["name"])
            break
        elif search == shop_libriry["web_camera"]["name"]:
            print(shop_libriry["web_camera"]["name"])
            break
        else:
            print("Товар не найден")
            break 


# Здание 3 

def task3():
    category = str(input("Введите товар: "))
    for key, value in shop_libriry.items():
        if category == "Внешние устройства":
            print(shop_libriry["mouse"], shop_libriry["keyboard"], shop_libriry["monitor"])
            break
        elif category == "Звук":
            print(shop_libriry["headphones"], shop_libriry["speakers"])
            break
        elif category == "Дополнительные устройства":
            print(shop_libriry["microphone"], shop_libriry["web_camera"])
            break
        elif category == "Файловый носитель":
            print(shop_libriry["usb_flash"])
            break
        else:
            print("Не удалось найти категорию")
            break


# Здание 4


def task4():
    for key in shop_libriry:
        if shop_libriry[key]["quantity"] == 0:
            print("На складе отсутствуют: ", shop_libriry[key]["name"], shop_libriry[key]["quantity"])
        elif 0 < shop_libriry[key]["quantity"] < 5:
            print("На скаладе товара меньше пяти и больше ноля: ", shop_libriry[key]["name"], shop_libriry[key]["quantity"])
        else: 
            print("На скаладе товара больше пяти: ", shop_libriry[key]["name"], shop_libriry[key]["quantity"])

# Здание 5

def task5():
    try:
        PersonalID = int(input("Введите ID: "))
    except ValueError:
        print("Ошибка: значения должены быть числами.")
        return
    itaration_status = False
    for key in shop_libriry:
        if PersonalID == shop_libriry[key]["id"]:
            PersonalQuantity = int(input("Введите количество единиц товара: "))
            shop_libriry[key]["quantity"] = PersonalQuantity + shop_libriry[key]["quantity"]
            print("Количество товаров изменино. Нынешнее количество товара ", shop_libriry[key]["name"], ": " , PersonalQuantity)
            itaration_status = True
            break
    if not itaration_status:
        print("Товар не найден")


# Здание 6

def task6():
    try:
        ClientID = int(input("Введите ID: "))
    except ValueError:
        print("Ошибка: значение должено быть числом.")
        return
    product_status = False
    for key in shop_libriry:
        if ClientID == shop_libriry[key]["id"]:
            ClientQuantity = int(input("Введите количество нужного вам товара: "))
            if ClientQuantity <= shop_libriry[key]["quantity"]:
                result = ClientQuantity *  shop_libriry[key]["price"]
                print("Ваш заказ на ", shop_libriry[key]["name"], " стомостью за штуку ", shop_libriry[key]["price"], 
                    " При количестве в ", ClientQuantity, " штуки, будет стоить: ", result)
                product_status = True
                break
            else:
                print("Количествва товара недостаточно, нынешнее количество данного товара: ", shop_libriry[key]["quantity"])
                product_status = True
                break
    if not product_status:
        print("Товар не найден")

# Здание 7

def task7():
    admin_request = str(input("Ввидете запрос: "))
    admin_status = False
    for key in shop_libriry:
        if admin_request == "общее количество различных товаров":
            print(shop_libriry[key]["name"])
        elif admin_request == "общее количество единиц продукции на складе":
            result = (shop_libriry["headphones"]["quantity"] + shop_libriry["keyboard"]["quantity"] 
                    + shop_libriry["microphone"]["quantity"] + shop_libriry["monitor"]["quantity"] 
                    + shop_libriry["mouse"]["quantity"] + shop_libriry["speakers"]["quantity"] 
                    + shop_libriry["usb_flash"]["quantity"] + shop_libriry["web_camera"]["quantity"])
            print("Товар: ", shop_libriry[key]["name"], " его количество на складе ", shop_libriry[key]["quantity"])
            print("Общее количество единиц продукции на складе: ", result)
        elif admin_request == "общую стоимость товаров на складе":
            total = ((shop_libriry["headphones"]["price"] * shop_libriry["headphones"]["quantity"]) + (shop_libriry["keyboard"]["price"] * shop_libriry["keyboard"]["quantity"]) 
            + (shop_libriry["microphone"]["price"] * shop_libriry["microphone"]["quantity"]) + (shop_libriry["monitor"]["price"] * shop_libriry["monitor"]["quantity"]) 
            + (shop_libriry["mouse"]["price"] * shop_libriry["mouse"]["quantity"]) + (shop_libriry["speakers"]["price"] * shop_libriry["speakers"]["quantity"]) 
            + (shop_libriry["usb_flash"]["price"] * shop_libriry["usb_flash"]["quantity"]) + (shop_libriry["web_camera"]["price"] * shop_libriry["web_camera"]["quantity"]))
            print("Общее стоимость товаров на складе: ", total)
        elif admin_request == "самый дорогой товар":
            total_price_list = []
            max_cost = [0, None]
            for key_2 in shop_libriry:
                total_price_list.append([shop_libriry[key_2]["price"], shop_libriry[key_2]["name"]])
            for index in total_price_list:
                if index[0] > max_cost[0]:
                    max_cost[0] = index[0]
                    max_cost[1] = index[1]
            print(max_cost)
            admin_status = True
            if not admin_status:
                print("Ошибка")
            break
        elif admin_request == "самый дешёвый товар":
            total_price_list_min = []
            for key_3 in shop_libriry:
                total_price_list_min.append([shop_libriry[key_3]["price"], shop_libriry[key_3]["name"]])
            min_cost = [total_price_list_min[0][0], None]
            for index2 in total_price_list_min:
                if index2[0] < min_cost[0]:
                    min_cost[0] = index2[0]
                    min_cost[1] = index2[1]
            print(min_cost)
            admin_status = True
            if not admin_status:
                print("Ошибка")
            break
        elif admin_request == "категорию, в которой находится больше всего товаров по количеству единиц":
            category_units = {}
            for key_4 in shop_libriry:
                cat = shop_libriry[key_4]["category"]
                if cat in category_units:
                    category_units[cat] = category_units[cat] + shop_libriry[key_4]["quantity"]
                else:
                    category_units[cat] = shop_libriry[key_4]["quantity"]
            best_cat = None
            best_units = -1
            for cat in category_units:
                if category_units[cat] > best_units:
                    best_units = category_units[cat]
                    best_cat = cat
            print("Категория с наибольшим количеством единиц: ", best_cat, " - ", best_units)
            admin_status = True
            if not admin_status:
                print("Ошибка")
            break
        elif admin_request == "среднюю цену одного товара в ассортименте":
            total_price = 0
            count = 0
            for key_5 in shop_libriry:
                total_price = total_price + shop_libriry[key_5]["price"]
                count = count + 1
            print("Средняя цена одного товара в ассортименте: ", total_price / count)
            admin_status = True
            if not admin_status:
                print("Ошибка")
            break
# Здание 8

def task8():
    print("1 - по цене (возр.)")
    print("2 - по цене (убыв.)")
    print("3 - по названию")
    print("4 - по количеству (возр.)")
    choice = input("Выберите способ сортировки: ")

    keys_list = []
    for key in shop_libriry:
        keys_list.append(key)

    if choice == "1":
        keys_list = sorted(keys_list, key=lambda k: shop_libriry[k]["price"])
    elif choice == "2":
        keys_list = sorted(keys_list, key=lambda k: shop_libriry[k]["price"], reverse=True)
    elif choice == "3":
        keys_list = sorted(keys_list, key=lambda k: shop_libriry[k]["name"])
    elif choice == "4":
        keys_list = sorted(keys_list, key=lambda k: shop_libriry[k]["quantity"])
    else:
        print("Неверный выбор")
        return

    for key in keys_list:
        print(shop_libriry[key]["name"], "| Цена:", shop_libriry[key]["price"], "| Количество:", shop_libriry[key]["quantity"])

# Здание 9

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
    elif taskEditor == "task3":
        task3()
        if (input("Еще раз?") != "Да"):
            status = False 
    elif taskEditor == "task4":
        task4()
        if (input("Еще раз?") != "Да"):
            status = False 
    elif taskEditor == "task5":
        task5()
        if (input("Еще раз?") != "Да"):
            status = False
    elif taskEditor == "task6":
        task6()
        if (input("Еще раз?") != "Да"):
            status = False
    elif taskEditor == "task7":
        task7()
        if (input("Еще раз?") != "Да"):
            status = False 
    elif taskEditor == "task8":
        task8()
        if (input("Еще раз?") != "Да"):
            status = False 
    else:
        print("Не удалось понять задачу")
        if (input("Еще раз?") != "Да"):
            status = False