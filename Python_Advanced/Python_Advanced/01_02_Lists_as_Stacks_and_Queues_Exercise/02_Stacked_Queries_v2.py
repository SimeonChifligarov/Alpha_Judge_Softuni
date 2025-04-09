from typing import List


def process_stack(queries: List[str]) -> List[int]:
    """
    Processes a list of stack operations like push, pop, find max and min.
    Returns the final stack state from top to bottom.
    """
    stack = []
    for query in queries:
        parts = query.split()
        if parts[0] == '1':
            stack.append(int(parts[1]))
        elif parts[0] == '2' and stack:
            stack.pop()
        elif parts[0] == '3' and stack:
            print(max(stack))
        elif parts[0] == '4' and stack:
            print(min(stack))
    return stack[::-1]


if __name__ == '__main__':
    number_of_queries_input = int(input())
    queries_input = [input() for _ in range(number_of_queries_input)]
    final_stack_output = process_stack(queries=queries_input)
    print(', '.join(str(element) for element in final_stack_output))
