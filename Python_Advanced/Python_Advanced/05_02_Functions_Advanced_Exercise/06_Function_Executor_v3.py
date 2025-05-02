def func_executor(*functions: tuple) -> str:
    """
    This function runs given functions with their arguments and shows results.

    Args:
        functions: Tuples where the first is a function and the second is its arguments

    Returns:
        A string with each function name and its result
    """
    results = [f'{func.__name__} - {func(*args)}' for func, args in functions]
    return '\n'.join(results)


# if __name__ == '__main__':
#     def add_numbers(a: int, b: int) -> int:
#         return a + b
#
#
#     def multiply_numbers(x: int, y: int) -> int:
#         return x * y
#
#
#     executed = func_executor(
#         (add_numbers, (5, 3)),
#         (multiply_numbers, (2, 4))
#     )
#     print(executed)
