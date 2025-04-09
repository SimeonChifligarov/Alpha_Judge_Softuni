from typing import List


def optimized_process_stack(operations: List[str]) -> List[int]:
    """
    Processes stack operations using additional stacks to quickly access
    maximum and minimum values. Returns the final stack from top to bottom.
    """
    stack = []
    max_stack = []
    min_stack = []
    for operation in operations:
        parts = operation.split()
        if parts[0] == '1':
            number = int(parts[1])
            stack.append(number)
            if not max_stack or number >= max_stack[-1]:
                max_stack.append(number)
            if not min_stack or number <= min_stack[-1]:
                min_stack.append(number)
        elif parts[0] == '2' and stack:
            removed = stack.pop()
            if removed == max_stack[-1]:
                max_stack.pop()
            if removed == min_stack[-1]:
                min_stack.pop()
        elif parts[0] == '3' and max_stack:
            print(max_stack[-1])
        elif parts[0] == '4' and min_stack:
            print(min_stack[-1])
    return stack[::-1]


if __name__ == '__main__':
    operations_count_input = int(input())
    operations_input = [input() for _ in range(operations_count_input)]
    final_stack_state_output = optimized_process_stack(operations=operations_input)
    print(', '.join(str(value) for value in final_stack_state_output))
