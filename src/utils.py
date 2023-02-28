from classes import *


data = {}
test = Store(data)
test.add("sprite унИкальный", 1)
test.add("cola", 10)
test.add("cola", 1)
test.remove("cola", 111)
print(test.items)
print(test.get_free_space())
print(test.get_items())
print(test.get_unique_items_count())