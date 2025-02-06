from typing import List


def rearrange_animal_parts(tail: str, body: str, head: str) -> List[str]:
    return [head, body, tail]


if __name__ == '__main__':
    tail_input = input()
    body_input = input()
    head_input = input()
    result = rearrange_animal_parts(tail=tail_input, body=body_input, head=head_input)
    print(result)
