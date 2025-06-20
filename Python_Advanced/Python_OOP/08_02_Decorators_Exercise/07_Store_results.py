from typing import Callable, Any


class StoreResults:
    """
    This class stores information about function calls into results.txt.
    """

    def __init__(self, function: Callable) -> None:
        self.function = function

    def __call__(self, *args, **kwargs) -> Any:
        result = self.function(*args, **kwargs)
        log_entry = f"Function '{self.function.__name__}' was called. Result: {result}\n"
        with open('results.txt', 'a') as file:
            file.write(log_entry)
        return result

    def __str__(self) -> str:
        return f'StoreResults for function {self.function.__name__}'

    def __repr__(self) -> str:
        return f'StoreResults(function={self.function.__name__})'


def store_results(function: Callable) -> Callable:
    """
    This function applies StoreResults to a function.
    Args:
        function (Callable): function to decorate
    Returns:
        Callable: decorated function
    """
    return StoreResults(function=function)


if __name__ == '__main__':
    @store_results
    def add(a: int, b: int) -> int:
        return a + b


    @store_results
    def mult(a: int, b: int) -> int:
        return a * b


    output = add(a=2, b=2)
    output = mult(a=6, b=4)
