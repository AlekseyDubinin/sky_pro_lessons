class Storage:  # хранилище

    def __init__(self, items: dict, capacity: int) -> None:
        self._items = items
        self._capacity = capacity

    def add(self, name_product: str, count: int) -> None:
        if name_product in self._items:
            self._items[name_product] += count
        else:
            self._items[name_product] = count

    def remove(self, name_product: str, count: int) -> bool:
        if count < self._items[name_product]:
            self._items[name_product] -= count
            return True
        else:
            return False

    @property
    def get_free_space(self) -> int:
        return self._capacity - sum(self._items.values())

    @property
    def get_items(self) -> dict:
        return self._items

    @property
    def get_unique_items_count(self) -> int:
        return len(self._items)


class Store(Storage):   # склад
    
    def __init__(self, items: dict, capacity: int = 100) -> None:
        super().__init__(items, capacity)

    def add(self, name_product: str, count: int) -> bool:
        if count <= self.get_free_space:
            super().add(name_product, count)
            return True
        else:
            return False


class Shop(Store):  # магазин
    def __init__(self, items: dict, capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, name_product: str, count: int) -> int:
        if name_product in self.get_items or self.get_unique_items_count < 5:
            return super().add(name_product, count)
        else:
            return False


class Request:  # формирование запроса
    def __init__(self, from1: str, to: str, amount: int, product: str) -> None:
        self.from1 = from1
        self.to = to
        self.amount = amount
        self.product = product

    def __repr__(self) -> str:
        return f'Доставить {self.amount} {self.product} из {self.from1} в {self.to}'
