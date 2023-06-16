from random import shuffle, randint


class BingoCase:

    def __init__(self, items):
        self._items = list(items)
        shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except ImportError:
            raise LookupError("Pick from an empty Bingo")

    def __call__(self, *args, **kwargs):
        return self.pick()


bingo = BingoCase(range(5))

print(bingo.pick())
print(bingo())
