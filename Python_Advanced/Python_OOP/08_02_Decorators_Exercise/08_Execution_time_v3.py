from typing import Callable, Any
import time


def exec_time(function: Callable) -> Callable:
    """
    This function measures how long the function execution takes.
    Args:
        function (Callable): function to decorate
    Returns:
        Callable: decorated function
    """

    def wrapper(*args, **kwargs) -> float:
        start_time = time.time()
        function(*args, **kwargs)
        end_time = time.time()
        return end_time - start_time

    return wrapper


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
