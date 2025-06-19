from typing import Callable, Any, Type


class TypeCheckDecorator:
    """
    This class checks if the argument matches the expected type.
    """

    def __init__(self, expected_type: Type) -> None:
        self.expected_type = expected_type

    def __call__(self, function: Callable) -> Callable:
        def wrapper(argument: Any) -> Any:
            if isinstance(argument, self.expected_type):
                return function(argument)
            return 'Bad Type'

        return wrapper

    def __str__(self) -> str:
        return f'TypeCheckDecorator for {self.expected_type}'

    def __repr__(self) -> str:
        return f'TypeCheckDecorator(expected_type={self.expected_type})'


def type_check(expected_type: Type) -> Callable[[Callable], Callable]:
    """
    This function applies TypeCheckDecorator to a function.
    Args:
        expected_type (Type): expected type for the function argument
    Returns:
        Callable: decorated function
    """
    return TypeCheckDecorator(expected_type=expected_type)

# if __name__ == '__main__':
#     @type_check(expected_type=int)
#     def times2(num: int) -> int:
#         return num * 2
#     output = times2(2)
#     print(output)
#     output = times2('Not A Number')
#     print(output)
#     @type_check(expected_type=str)
#     def first_letter(word: str) -> str:
#         return word[0]
#     output = first_letter('Hello World')
#     print(output)
#     output = first_letter(['Not', 'A', 'String'])
#     print(output)
#     pass
