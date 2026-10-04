class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._size = 0
        if capacity < 0:
            raise ValueError

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        self._size += n
        if self._size > self._capacity:
            raise ValueError

    def withdraw(self, n):
        if self._size < n:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

# I noticed that there was a recursion error in my code and I heard that putting a
# "_" after "." fixes it, so I tried and it worked!
