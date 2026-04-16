from src.stack_exceptions import StackEmptyException, StackFullException
from src.calculable_strategy import CalculableStrategy


class CustomStack:

    def __init__(self, limit, calculable_strategy: CalculableStrategy):
        self._limit = limit
        self._index = 0
        self._elements = []
        self._calculable_strategy = calculable_strategy

    def push(self, element):
        if self.size() == self._limit:
            raise StackFullException()
        self._elements.append(self._calculable_strategy.calculate_value(element))
        self._index += 1

    def pop(self):
        if self.is_empty():
            raise StackEmptyException()
        self._index -= 1
        return self._elements.pop(self._index)

    def is_empty(self):
        return len(self._elements) == 0

    def top(self):
        return self._elements[self._index - 1]

    def size(self):
        return len(self._elements)
