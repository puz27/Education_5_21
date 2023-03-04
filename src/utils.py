from classes import *
data_1 = {"фанта": 20, "кола": 100, "спрайт": 50}
data_2 = {}
my_store = Store(data_1)
my_shop = Shop(data_2)

input_data = ""
while True:
    input_data = input("Введите количество и название\n")
    if input_data == "стоп":
        break
    else:
        user = Request(input_data.split()[0], input_data.split()[1])
        print(user.info())
        print("-------------------------------------------")

        my_store.remove(user.info()[0], int(user.info()[1]))
        my_shop.add(user.info()[0], int(user.info()[1]))


        print("-------------------------------------------")
        print("СКЛАД:", my_store.get_items())
        print("МАГАЗИН:", my_shop.get_items())

