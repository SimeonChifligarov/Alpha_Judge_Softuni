def func_executor(*tasks: tuple) -> str:
    """
    This function executes functions with given arguments and collects their outputs.

    Args:
        tasks: Tuples with a function and a tuple of arguments for that function

    Returns:
        A string with function names and their results
    """
    output = []
    for function_item, arguments_item in tasks:
        result = function_item(*arguments_item)
        output.append(f'{function_item.__name__} - {result}')
    return '\n'.join(output)

# if __name__ == '__main__':
#     def sum_values(n_1: int, n_2: int) -> int:
#         return n_1 + n_2
#
#
#     def divide_values(v_1: int, v_2: int) -> float:
#         return v_1 / v_2
#
#
#     results = func_executor(
#         (sum_values, (10, 20)),
#         (divide_values, (50, 5))
#     )
#     print(results)
