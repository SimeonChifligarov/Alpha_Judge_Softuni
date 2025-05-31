class Integer:
    def __init__(self, int_value):
        self.value = int_value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return 'value is not a float'

        floored_value = int(float_value)
        return cls(floored_value)

    @classmethod
    def from_roman(cls, roman_value):
        roman_numerals = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000,
        }
        result = 0
        previous_value = 0
        for letter in reversed(roman_value.upper()):
            current_value = roman_numerals.get(letter, 0)
            if current_value < previous_value:
                result -= current_value
            else:
                result += current_value
            previous_value = current_value

        return cls(result)

    @classmethod
    def from_string(cls, string_value):
        if not isinstance(string_value, str):
            return 'wrong type'

        try:
            parsed_value = int(string_value)
            return cls(parsed_value)
        except ValueError:
            return 'wrong type'
