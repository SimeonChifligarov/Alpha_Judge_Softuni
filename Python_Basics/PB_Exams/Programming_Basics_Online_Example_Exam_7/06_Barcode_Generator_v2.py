# # BAD PROBLEM DESCRIPTION!
# # does not give 100/100 in automatic system
#
# def generate_barcodes(start_range, end_range):
#     barcodes = []
#
#     for barcode in range(start_range, end_range + 1):
#         barcode_str = str(barcode)
#         if all(int(digit) % 2 != 0 for digit in barcode_str):
#             barcodes.append(barcode_str)
#
#     return ' '.join(barcodes)


def generate_barcodes(start_range, end_range):
    result = []

    start_range_digits = [int(d) for d in str(start_range)]
    end_range_digits = [int(d) for d in str(end_range)]

    for d1 in range(start_range_digits[0], end_range_digits[0] + 1):
        if d1 % 2 == 0:
            continue
        for d2 in range(start_range_digits[1], end_range_digits[1] + 1):
            if d2 % 2 == 0:
                continue
            for d3 in range(start_range_digits[2], end_range_digits[2] + 1):
                if d3 % 2 == 0:
                    continue
                for d4 in range(start_range_digits[3], end_range_digits[3] + 1):
                    if d4 % 2 == 0:
                        continue
                    result.append(f'{d1}{d2}{d3}{d4}')

    return ' '.join(result)


if __name__ == '__main__':
    start_range_input = int(input())
    end_range_input = int(input())

    res = generate_barcodes(
        start_range=start_range_input,
        end_range=end_range_input,
    )
    print(res)
