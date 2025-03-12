def collect_resources() -> dict[str, int]:
    """
    Collects resources and their quantities from user input until 'stop' is received.
    """
    resources = {}
    while True:
        resource = input()
        if resource == 'stop':
            break
        quantity = int(input())
        resources[resource] = resources.get(resource, 0) + quantity
    return resources


def print_resources(resources: dict[str, int]) -> None:
    """
    Prints resources and their quantities in the required format.
    """
    for resource, quantity in resources.items():
        print(f'{resource} -> {quantity}')


if __name__ == '__main__':
    result = collect_resources()
    print_resources(resources=result)
