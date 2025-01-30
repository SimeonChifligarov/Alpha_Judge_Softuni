def print_triples(n: int) -> list[str]:
    result = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result.append(f'{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}')
    return result


if __name__ == '__main__':
    count = int(input())
    output_list = print_triples(n=count)
    print('\n'.join(output_list))
