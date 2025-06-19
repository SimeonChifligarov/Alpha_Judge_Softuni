from typing import Callable, Any, Type


def type_check(expected_type: Type) -> Callable[[Callable], Callable]:
    """
    This function checks if the argument matches the expected type.
    Args:
        expected_type (Type): expected type for the function argument
    Returns:
        Callable: decorated function
    """

    def decorator(function: Callable) -> Callable:
        def wrapper(argument: Any) -> Any:
            if isinstance(argument, expected_type):
                return function(argument)
            return 'Bad Type'

        return wrapper

    return decorator

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
