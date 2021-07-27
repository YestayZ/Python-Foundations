from abc import ABC, abstractmethod


class Dress(ABC):
    def __init__(self, size):
        self.size = size

    @property
    @abstractmethod
    def consume(self):
        pass

    def __add__(self, other):
        return self.size + other.size


class Coat(Dress):
    @property
    def consume(self):
        return round((self.size / 6.5) + 0.5)


class Suit(Dress):
    @property
    def consume(self):
        return round((2 * self.size + 0.3) / 100)


coat = Coat(56)
suit = Suit(200)
print(coat.consume)
print(coat + suit)
