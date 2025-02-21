def get_proper_divisors(number: int) -> list:
    """Returns a list of proper divisors of a given number (excluding itself)."""
    return [n for n in range(1, number // 2 + 1) if number % n == 0]


def is_perfect_number(number: int) -> bool:
    """Checks if a given number is a perfect number."""
    return sum(get_proper_divisors(number)) == number


def main():
    """Handles user input and prints the result based on the perfect number check."""
    number = int(input())
    if is_perfect_number(number):
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


if __name__ == "__main__":
    main()
