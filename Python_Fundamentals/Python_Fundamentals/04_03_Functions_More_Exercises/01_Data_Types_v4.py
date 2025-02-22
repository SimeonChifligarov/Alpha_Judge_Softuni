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
        if isinstance(value, int):
            return str(value * 2)
        elif isinstance(value, float):
            return f'{value * 1.5:.2f}'
        elif isinstance(value, str):
            return f'${value}$'
        return ''


if __name__ == '__main__':
    type_input = input()
    value_input = input()

    processor_instance = Processor()

    processed_output = ''
    if type_input == 'int':
        processed_output = processor_instance.process(value=int(value_input))
    elif type_input == 'real':
        processed_output = processor_instance.process(value=float(value_input))
    elif type_input == 'string':
        processed_output = processor_instance.process(value=value_input)

    print(processed_output)
