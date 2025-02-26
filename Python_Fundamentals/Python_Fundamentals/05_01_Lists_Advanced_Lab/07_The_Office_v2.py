def evaluate_employee_happiness():
    """
    Reads a list of employee happiness levels and an improvement factor.
    Computes the adjusted happiness levels and determines if employees are happy.
    """
    happiness_levels = list(map(int, input().split()))
    improvement_factor = int(input())

    adjusted_happiness = [level * improvement_factor for level in happiness_levels]
    average_happiness = sum(adjusted_happiness) / len(adjusted_happiness)

    happy_employees = [level for level in adjusted_happiness if level >= average_happiness]
    total_employees = len(adjusted_happiness)
    happy_count = len(happy_employees)

    print(
        f'Score: {happy_count}/{total_employees}. '
        f'Employees are {"happy" if happy_count >= total_employees / 2 else "not happy"}!'
    )


if __name__ == '__main__':
    evaluate_employee_happiness()
