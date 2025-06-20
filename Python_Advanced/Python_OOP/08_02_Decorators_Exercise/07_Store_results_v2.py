from typing import Callable, Any


class StoreResults:
    """
    This class stores info about function calls into results.txt file.
    """

    def __init__(self, function: Callable) -> None:
        self.function = function

    def __call__(self, *args, **kwargs) -> Any:
        result = self.function(*args, **kwargs)
        self._write_to_file(function_name=self.function.__name__, function_result=result)
        return result

    @staticmethod
    def _write_to_file(function_name: str, function_result: Any) -> None:
        """
        This static method writes function call info into the results file.
        Args:
            function_name (str): name of the function called
            function_result (Any): result of the function
        """
        with open('results.txt', 'a') as file:
            file.write(f"Function '{function_name}' was called. Result: {function_result}\n")

    def __str__(self) -> str:
        return f'StoreResults for {self.function.__name__}'

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
