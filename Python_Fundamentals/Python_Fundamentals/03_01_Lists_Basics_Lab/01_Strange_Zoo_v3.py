from typing import List


def rearrange_animal_parts(parts: List[str]) -> List[str]:
    parts[0], parts[2] = parts[2], parts[0]
    return parts


if __name__ == '__main__':
    tail_input = input()
    body_input = input()
    head_input = input()
    parts_input = [tail_input, body_input, head_input]
    result = rearrange_animal_parts(parts=parts_input)
    print(result)
