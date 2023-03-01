from classes import *


data = {}
test = Store(data)

test.add("sprite унИкальный", 3)
test.add("sprite унИкальный", 9)
test.add("cola", 11)
test.add("cola", 10)
print(test.get_free_space())
print(test.get_items())

#test2 = Shop(data2)
#data2 = {}
# print("-----")
# print(test2.capacity)
# test2.add("cola", 2)
# test2.add("cola2", 1)
# test2.add("cola3", 1)
# test2.add("cola4", 1)
# test2.add("cola77", 19)
# test2.add("cola771", 1)
# print(test2.items)

r = {}


# def get_free_space(items):
#     capacity = 100
#     for item in items.values():
#         print(item)
#         capacity -= item
#     return capacity
#
# print(get_free_space(r))