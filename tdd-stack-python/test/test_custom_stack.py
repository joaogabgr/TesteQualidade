import pytest
from unittest.mock import MagicMock
from src.custom_stack import CustomStack
from src.calculable_strategy import CalculableStrategy
from src.stack_exceptions import StackEmptyException, StackFullException


@pytest.fixture
def mock_strategy():
    """Mock do CalculableStrategy — equivalente ao @Mock do Mockito."""
    strategy = MagicMock(spec=CalculableStrategy)
    strategy.calculate_value.side_effect = lambda v: v
    return strategy


@pytest.fixture
def double_strategy():
    """Mock que dobra o valor — testa que push usa a strategy."""
    strategy = MagicMock(spec=CalculableStrategy)
    strategy.calculate_value.side_effect = lambda v: v * 2
    return strategy


class TestCustomStack:

    def test_new_stack_is_empty(self, mock_strategy):
        stack = CustomStack(5, mock_strategy)
        assert stack.is_empty() is True
        assert stack.size() == 0

    def test_push_one_element(self, mock_strategy):
        stack = CustomStack(5, mock_strategy)
        stack.push(10)
        assert stack.is_empty() is False
        assert stack.size() == 1
        assert stack.top() == 10

    def test_push_calls_calculable_strategy(self, mock_strategy):
        stack = CustomStack(5, mock_strategy)
        stack.push(42)
        mock_strategy.calculate_value.assert_called_once_with(42)

    def test_push_stores_transformed_value(self, double_strategy):
        stack = CustomStack(5, double_strategy)
        stack.push(10)
        assert stack.top() == 20

    def test_push_multiple_elements(self, mock_strategy):
        stack = CustomStack(5, mock_strategy)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.size() == 3

    def test_push_raises_stack_full_exception(self, mock_strategy):
        stack = CustomStack(2, mock_strategy)
        stack.push(1)
        stack.push(2)
        with pytest.raises(StackFullException):
            stack.push(3)

    def test_pop_returns_last_element(self, mock_strategy):
        stack = CustomStack(5, mock_strategy)
        stack.push(10)
        stack.push(20)
        assert stack.pop() == 20
        assert stack.size() == 1

    def test_pop_empty_stack_raises_exception(self, mock_strategy):
        stack = CustomStack(5, mock_strategy)
        with pytest.raises(StackEmptyException):
            stack.pop()

    def test_top_returns_last_without_removing(self, mock_strategy):
        stack = CustomStack(5, mock_strategy)
        stack.push(99)
        assert stack.top() == 99
        assert stack.size() == 1

    def test_push_pop_lifo_order(self, mock_strategy):
        stack = CustomStack(3, mock_strategy)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1

    def test_strategy_raises_null_pointer(self, mock_strategy):
        """Simula NullPointerException do Java — strategy lança exceção."""
        mock_strategy.calculate_value.side_effect = TypeError("value is None")
        stack = CustomStack(5, mock_strategy)
        with pytest.raises(TypeError):
            stack.push(None)


class TestCalculableStrategy:

    def test_concrete_strategy_implementation(self):
        """Testa uma implementação concreta do CalculableStrategy."""

        class DoubleStrategy(CalculableStrategy):
            def calculate_value(self, value):
                return value * 2

        strategy = DoubleStrategy()
        assert strategy.calculate_value(5) == 10
