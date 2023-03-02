from classes import *
#
# #
# data = {}
# test = Store(data)
#
# test.add("sprite унИкальный", 3)
# test.add("sprite унИкальный", 9)
# test.add("cola", 11)
# test.add("cola", 10)
# print(test.get_free_space())
# print(test.get_items())
data2 = {"тестовый товар": 5}
test2 = Shop(data2)
print("-----")
print(test2.capacity)
test2.add("cola", 5)
test2.add("cola", 5)
test2.add("cola", 1)
test2.add("sprite", 1)



print(test2.get_items())
