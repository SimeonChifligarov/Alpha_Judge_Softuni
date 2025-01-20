def greet_user(name):
    if name == 'Johnny':
        return 'Hello, my love!'
    return f'Hello, {name}!'


if __name__ == '__main__':
    name_input = input()
    print(greet_user(name=name_input))
