class Stack:
    """
    This class is about a simple stack where you can push and pop items.

    Methods:
        push(el): Adds an item to the stack.
        pop(): Removes and returns the top item.
        top(): Returns the top item without removing it.
        is_empty(): Checks if the stack is empty.
    """

    def __init__(self) -> None:
        self.data = []

    def push(self, el: str) -> None:
        self.data.append(el)

    def pop(self) -> str:
        el = self.data.pop()
        return el

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def __str__(self) -> str:
        result_str = f'[{", ".join(reversed(self.data))}]'
        return result_str


if __name__ == '__main__':
    # stack_instance = Stack()
    # stack_instance.push('one')
    # stack_instance.push('two')
    # print(stack_instance.pop())
    # print(stack_instance)
    pass
