import pytest
from src.custom_stack_class import CustomStack, StackEmptyException, StackFullException


class TestCustomStack:

    def test_new_stack_is_empty(self):
        stack = CustomStack(3)
        assert stack.is_empty() is True
        assert stack.size() == 0

    def test_push_one_element(self):
        stack = CustomStack(5)
        stack.push(5.0)
        assert stack.is_empty() is False
        assert stack.top() == 5.0
        assert stack.size() == 1

    def test_push_multiple_elements(self):
        stack = CustomStack(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.size() == 3

    def test_push_raises_stack_full_exception(self):
        stack = CustomStack(2)
        stack.push(1)
        stack.push(2)
        with pytest.raises(StackFullException):
            stack.push(3)

    def test_pop_returns_last_element(self):
        stack = CustomStack(5)
        stack.push(10)
        stack.push(20)
        assert stack.pop() == 20
        assert stack.size() == 1

    def test_pop_empty_stack_raises_exception(self):
        stack = CustomStack(5)
        with pytest.raises(StackEmptyException):
            stack.pop()

    def test_top_returns_last_without_removing(self):
        stack = CustomStack(5)
        stack.push(42)
        assert stack.top() == 42
        assert stack.size() == 1

    def test_top_empty_stack_raises_exception(self):
        stack = CustomStack(5)
        with pytest.raises(StackEmptyException):
            stack.top()

    def test_push_pop_lifo_order(self):
        stack = CustomStack(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1
