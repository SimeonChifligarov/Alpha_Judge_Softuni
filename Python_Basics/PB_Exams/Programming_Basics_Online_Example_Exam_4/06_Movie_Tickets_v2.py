def generate_tickets(a1, a2, n):
    for symbol1_ascii in range(a1, a2):
        for symbol2 in range(1, n):
            for symbol3 in range(1, n // 2):
                symbol4 = symbol1_ascii
                if symbol1_ascii % 2 != 0 and (symbol2 + symbol3 + symbol4) % 2 != 0:
                    print(f'{chr(symbol1_ascii)}-{symbol2}{symbol3}{symbol4}')


a1_input = int(input())
a2_input = int(input())
n_input = int(input())
generate_tickets(a1=a1_input, a2=a2_input, n=n_input)
