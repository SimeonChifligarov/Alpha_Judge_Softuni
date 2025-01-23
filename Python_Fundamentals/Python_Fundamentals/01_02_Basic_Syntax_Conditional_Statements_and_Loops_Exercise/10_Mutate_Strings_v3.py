def transform_strings(original, target):
    result = list(original)
    last_printed = original
    transformations = []
    for i in range(len(original)):
        if result[i] != target[i]:
            result[i] = target[i]
            current_string = ''.join(result)
            if current_string != last_printed:
                transformations.append(current_string)
                last_printed = current_string
    return transformations


if __name__ == '__main__':
    first_string = input()
    second_string = input()
    transformations_output = transform_strings(original=first_string, target=second_string)
    for transformation in transformations_output:
        print(transformation)
