class Heap:
    def __init__(self):
        self._values = []
        self._size = 0

    def insert(self, value):
        self._values.append(value)
        self._size += 1
        self.shift_up(self._size - 1)

    def pop(self):
        tmp = self._values[0]
        self._values[0] = self._values[-1]
        self._values.pop()
        self._size -= 1
        self.shift_down(0)
        return tmp

    def shift_up(self, i):
        while i != 0 and self._values[i] < self._values[(i-1)//2]:
            self._values[i], self._values[(i-1)//2] = (self._values[(i-1)//2], 
                                                       self._values[i])
            i = (i-1)//2

    def shift_down(self, i):
        while 2*i+1 < self._size:
            j = i
            if self._values[2*i+1] < self._values[i]:
                j = 2*i+1
            if 2*i+2 < self._size and self._values[2*i+2] < self._values[j]:
                j = 2*i+2
            if i == j:
                break
            self._values[i], self._values[j] = self._values[j], self._values[i]


if __name__ == '__main__':
    h = Heap()
    h.insert(5)
    h.insert(3)
    h.insert(7)
    h.insert(1)
    h.insert(2)

    assert 1 == h.pop()
    assert 2 == h.pop()
    assert 3 == h.pop()
    assert 5 == h.pop()
    assert 7 == h.pop()
