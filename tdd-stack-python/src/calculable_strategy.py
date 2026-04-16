from abc import ABC, abstractmethod


class CalculableStrategy(ABC):

    @abstractmethod
    def calculate_value(self, value):
        """Transforma o valor antes de empilhar. Equivalente ao CalculableStrategy<T> do Java."""
        ...
