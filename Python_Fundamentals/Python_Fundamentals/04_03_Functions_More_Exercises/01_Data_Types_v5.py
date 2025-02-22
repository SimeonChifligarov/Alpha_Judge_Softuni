from functools import singledispatch


@singledispatch
def process(value) -> str:
    return ''


@process.register
def _(value: int) -> str:
    return str(value * 2)


@process.register
def _(value: float) -> str:
    return f'{value * 1.5:.2f}'


@process.register
def _(value: str) -> str:
    return f'${value}$'


if __name__ == '__main__':
    type_input = input()
    value_input = input()

    converted_value = (
        int(value_input) if type_input == 'int'
        else float(value_input) if type_input == 'real'
        else value_input
    )

    print(process(converted_value))
