from typing import Callable, Any
import timeit


class ExecutionTimer:
    """
    This class measures how long the function execution takes using timeit.
    """

    def __init__(self, function: Callable) -> None:
        self.function = function

    def __call__(self, *args, **kwargs) -> float:
        start = timeit.default_timer()
        self.function(*args, **kwargs)
        end = timeit.default_timer()
        return end - start

    def __str__(self) -> str:
        return f'ExecutionTimer for function {self.function.__name__}'

    def __repr__(self) -> str:
        return f'ExecutionTimer(function={self.function.__name__})'


def exec_time(function: Callable) -> Callable:
    """
    This function applies ExecutionTimer to a function.
    Args:
        function (Callable): function to decorate
    Returns:
        Callable: decorated function
    """
    return ExecutionTimer(function=function)


if __name__ == '__main__':
    @exec_time
    def loop(start: int, end: int) -> int:
        total = 0
        for x in range(start, end):
            total += x
        return total


    output = loop(start=1, end=10000000)
    print(output)


    @exec_time
    def concatenate(strings: list[str]) -> str:
        result = ''
        for string in strings:
            result += string
        return result


    output = concatenate(strings=['a' for _ in range(1000000)])
    print(output)


    @exec_time
    def loop() -> None:
        count = 0
        for i in range(1, 9999999):
            count += 1


    output = loop()
    print(output)
