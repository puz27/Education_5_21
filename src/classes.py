from abc import ABC


class Storage(ABC):


    def __init__(self, items: dict):
        self.items = items
        self.capacity = 100

    def add(self, description: str, count: int):
        if self.items.get(description, False) is False:
            self.items[description] = count
        else:
            self.items[description] = self.items[description] + count

    def remove(self, description: str, count: int):
        if self.items.get(description, False) is False:
            print("No this items")
        else:
            if self.items[description] - count <= 0:
                del self.items[description]
            else:
                self.items[description] = self.items[description] - count

    def get_free_space(self):
        for item in self.items.values():
            self.capacity -= item
        return self.capacity

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        unique_items = []
        for item in self.items:
            if "уникальн" in item.lower():
                unique_items.append(item)
            return unique_items


class Store(Storage):
    capacity = 100

class Shop(Storage):
    capacity = 20