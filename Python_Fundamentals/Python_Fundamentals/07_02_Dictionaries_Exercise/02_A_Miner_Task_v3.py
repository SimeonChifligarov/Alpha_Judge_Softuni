from collections import defaultdict


def collect_resources() -> dict[str, int]:
    """
    Collects resources and their quantities from user input until 'stop' is received.
    """
    resources = defaultdict(int)

    while True:
        resource = input()
        if resource == 'stop':
            break
        quantity = int(input())
        resources[resource] += quantity
    return dict(resources)


def print_resources(resources: dict[str, int]) -> None:
    """
    Prints resources and their quantities in the required format.
    """
    for resource, quantity in resources.items():
        print(f'{resource} -> {quantity}')


if __name__ == '__main__':
    result = collect_resources()
    print_resources(resources=result)
