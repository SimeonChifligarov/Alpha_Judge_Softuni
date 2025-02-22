class Processor:
    """
    A class that processes different types of input using method overloading.
    """

    @staticmethod
    def process(value) -> str:
        """
        Processes the input based on its type.

        :param value: The value to be processed (int, float, or str).
        :return: The processed result as a string.
        """
        process_functions = {
            int: lambda v: str(v * 2),
            float: lambda v: f'{v * 1.5:.2f}',
            str: lambda v: f'${v}$',
        }

        return process_functions.get(type(value), lambda v: '')(value)


if __name__ == '__main__':
    type_mapping = {
        'int': int,
        'real': float,
        'string': str,
    }

    type_input = input()
    value_input = input()

    processor_instance = Processor()
    cast_func = type_mapping.get(type_input, lambda v: v)
    processed_output = processor_instance.process(cast_func(value_input))

    print(processed_output)
