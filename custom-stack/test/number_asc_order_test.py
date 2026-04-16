import pytest
from unittest.mock import MagicMock
from src.custom_stack_class import CustomStack
from src.number_asc_order import NumberAscOrder


class TestNumberAscOrder:

    def test_sort_stack_with_6_random_numbers(self):
        numbers = [45, 12, 33, 7, 58, 21]

        stack = CustomStack(6)
        for n in numbers:
            stack.push(n)

        sorter = NumberAscOrder()
        result = sorter.sort(stack)

        assert result == [7, 12, 21, 33, 45, 58]
        assert stack.is_empty() is True

    def test_sort_empty_stack_with_capacity_6(self):
        stack = CustomStack(6)

        sorter = NumberAscOrder()
        result = sorter.sort(stack)

        assert result == []
        assert stack.is_empty() is True

    def test_sort_with_mock_stack_6_numbers(self):
        """Usando Mock Object para simular a CustomStack"""
        numbers = [45, 12, 33, 7, 58, 21]

        mock_stack = MagicMock(spec=CustomStack)
        mock_stack.is_empty.side_effect = [False, False, False, False, False, False, True]
        mock_stack.pop.side_effect = [21, 58, 7, 33, 12, 45]

        sorter = NumberAscOrder()
        result = sorter.sort(mock_stack)

        assert result == [7, 12, 21, 33, 45, 58]
        assert mock_stack.pop.call_count == 6

    def test_sort_with_mock_empty_stack(self):
        """Usando Mock Object para simular uma CustomStack vazia"""
        mock_stack = MagicMock(spec=CustomStack)
        mock_stack.is_empty.return_value = True

        sorter = NumberAscOrder()
        result = sorter.sort(mock_stack)

        assert result == []
        mock_stack.pop.assert_not_called()

    def test_sort_raises_type_error_for_invalid_param(self):
        sorter = NumberAscOrder()
        with pytest.raises(TypeError):
            sorter.sort([1, 2, 3])
