from src.custom_stack_class import CustomStack


class NumberAscOrder:

    def sort(self, stack: CustomStack) -> list:
        if not isinstance(stack, CustomStack):
            raise TypeError("Parameter must be a CustomStack")

        result = []
        while not stack.is_empty():
            result.append(stack.pop())

        result.sort()
        return result
