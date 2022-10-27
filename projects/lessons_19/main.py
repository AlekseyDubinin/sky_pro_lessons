class DinArray:

    def __init__(self, *args, size=0):
        _len = 0
        for _ in args:
            _len += 1
        self._len = _len
        self.size = max(_len, size)
        self._args = [x for x in args] + [None] * (self.size - self._len)
        self._free = self.size - self._len

    def __repr__(self):
        return f'[{", ".join(map(str, (x for x in self._args if x is not None)))}]'

    def __len__(self):
        return self._len

    def push(self, x):
        if self._free == 0:
            self._resize()
        self._args[self._len] = x
        self._len += 1
        self._free -= 1

    def _resize(self):
        self._args += [None] * self.size
        self.size = self.size * 2
        self._free += self.size

    def pop(self, index=-1):
        if index > self._len - 1:
            raise IndexError
        if index == -1:
            num = self._args[self._len - 1]
        else:
            num = self._args[index]
            for i in range(index, self._len - 1):
                self._args[i] = self._args[i + 1]
        self._args[self._len - 1] = None
        self._free += 1
        self._len -= 1
        return num

    def insert(self, index, x):
        if self._free == 0:
            self._resize()
        if index > self._len - 1:
            self.push(x)
            return
        for i in range(self._len - 1, index - 1, -1):
            self._args[i + 1] = self._args[i]
        self._args[index] = x
        self._len += 1
        self._free -= 1

    def __add__(self, other):
        if not isinstance(other, DinArray):
            raise TypeError
        size = self._len + other._len
        newarr = DinArray(size=size)
        i = 0
        for arg in self._args[:self._len]:
            newarr._args[i] = arg
            i += 1
        for arg in other._args[:other._len]:
            newarr._args[i] = arg
            i += 1
        newarr._len = size
        return newarr

    def __getitem__(self, item):
        if item >= self._len or item <= -self._len - 1 or item == 0:
            raise IndexError
        if item > 0:
            return self._args[item - 1]
        else:
            return self._args[item]



a = DinArray(2, 5, 6, size=10)
print(a)
print(len(a))
print(a.size)
a.push(7)
print(a)
print(a._free)
print(a.pop())
print(a)
a.push(9)
print(a)
print(a.pop(1))
print(a)
a.insert(1, 5)
print(a)
a.insert(5, 5)
print(a)
b = DinArray(1, 4, 8, 10)
c = a + b
print(c)
print(c.size)
print(len(c))
print(c[5])
print(c[-2])

