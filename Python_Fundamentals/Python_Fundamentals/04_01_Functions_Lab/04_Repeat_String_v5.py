repeat_string = lambda text, count: text * count

if __name__ == '__main__':
    input_text = input()
    input_count = int(input())
    output = repeat_string(text=input_text, count=input_count)
    print(output)
