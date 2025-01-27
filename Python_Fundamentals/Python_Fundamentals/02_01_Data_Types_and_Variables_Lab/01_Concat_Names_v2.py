def join_names(name_1, name_2, delimiter):
    return name_1 + delimiter + name_2


if __name__ == '__main__':
    first_name = input()
    second_name = input()
    separator = input()
    result = join_names(name_1=first_name, name_2=second_name, delimiter=separator)
    print(result)
