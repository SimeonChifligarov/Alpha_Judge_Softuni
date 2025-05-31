from typing import Union


class Integer:
    """This class helps to create an integer number from int, float, roman or string."""

    def __init__(self, int_value: int) -> None:
        self.value: int = int_value

    @classmethod
    def from_float(cls, float_value: float) -> Union['Integer', str]:
        if not isinstance(float_value, float):
            return 'value is not a float'

        floored_value: int = int(float_value)
        return cls(floored_value)

    @classmethod
    def from_roman(cls, roman_value: str) -> 'Integer':
        roman_numerals: dict[str, int] = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000,
        }
        result: int = 0
        previous_value: int = 0
        for letter in reversed(roman_value.upper()):
            current_value: int = roman_numerals.get(letter, 0)
            if current_value < previous_value:
                result -= current_value
            else:
                result += current_value
            previous_value = current_value

        return cls(result)

    @classmethod
    def from_string(cls, string_value: str) -> Union['Integer', str]:
        if not isinstance(string_value, str):
            return 'wrong type'

        try:
            parsed_value: int = int(string_value)
            return cls(parsed_value)
        except ValueError:
            return 'wrong type'


if __name__ == '__main__':
    # first_num_instance = Integer(int_value=10)
    # print(first_num_instance.value)
    # second_num_instance = Integer.from_roman(roman_value='IV')
    # print(second_num_instance.value)
    # print(Integer.from_float(float_value='2.6'))
    # print(Integer.from_string(string_value=2.6))
    pass
