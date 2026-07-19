class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items: dict[int, int] = {}

    def get(self, key: int) -> int:
        if key in self.items:
            value = self.items.pop(key)
            self.items[key] = value
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            self.items.pop(key)
            self.items[key] = value
        else:
            if len(self.items) == self.capacity:
                # iterator = iter(self.items)
                # least_recent_key = next(iterator)
                # self.items.pop(least_recent_key)
                self.items.pop(next(iter(self.items)))
            self.items[key] = value