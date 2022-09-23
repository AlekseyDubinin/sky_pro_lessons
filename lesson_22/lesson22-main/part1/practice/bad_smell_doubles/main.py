class SomeClass:
    def __init__(self):
        self.lst = [3, 2, 1, 4, 2, 1]

    def sorted_func(self):
        return sorted(self.lst, reverse=False)
