if __name__ == '__main__':
    input_text = input()
    input_count = int(input())
    print((lambda text, count: text * count)(text=input_text, count=input_count))
