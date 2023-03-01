from abc import ABC, abstractmethod


class Storage(ABC):


    def __init__(self, items: dict):
        self.items = items
        self.capacity = 200

    def add(self, description: str, count: int):
        # check item for availability and space

        # add new item and check space
        if self.items.get(description, False) is False:
            if count >= self.get_free_space():
                print("No free space")
            else:
                self.items[description] = count
        # add existing item and check space
        else:
            if self.items[description] + count >= self.get_free_space():
                print("No free space")
            else:
                self.items[description] = self.items[description] + count


    def remove(self, description: str, count: int):

        # not found item
        if self.items.get(description, False) is False:
            print("No this items")
        # found item delete need counts
        else:
            if self.items[description] - count <= 0:
                del self.items[description]
            else:
                self.items[description] = self.items[description] - count

    def get_free_space(self):
        all_space = self.capacity
        busy_free_space = 0
        for item in self.items.values():
            busy_free_space += item

        return all_space - busy_free_space

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        unique_items = 0
        for item, value in self.items.items():
            if "уникальн" in item.lower():
                unique_items += value
        return unique_items


class Store(Storage):
    def __init__(self, items: dict):
        super().__init__(items)
        self.capacity = 100
class Shop(Storage):

    def __init__(self, items: dict):
        super().__init__(items)
        self.capacity = 20

    def add(self, description: str, count: int):
        # check item for availability and space

        # add new item and check space
        if self.items.get(description, False) is False:
            if count >= self.capacity:
                print("No free space")
            elif len(self.items) > 5:
                print("Different items more than 5!")
            else:
                self.items[description] = count
        # add existing item and check space
        else:
            if self.items[description] + count >= self.capacity:
                print("No free space")
            elif len(self.items) > 5:
                print("Different items more than 5!")
            else:
                self.items[description] = self.items[description] + count
