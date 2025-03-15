def register_employees() -> dict[str, list[str]]:
    """
    Reads company names and employee IDs from input.
    Returns a dictionary where keys are company names and values are sets of unique employee IDs.
    """
    companies = {}

    while True:
        data = input()
        if data == 'End':
            break

        company_name, employee_id = data.split(' -> ', maxsplit=1)

        if company_name not in companies:
            companies[company_name] = []

        if employee_id not in companies[company_name]:
            companies[company_name].append(employee_id)

    return companies


def print_companies(companies: dict[str, list[str]]) -> None:
    """
    Prints each company name and its employees' IDs.
    """
    for company, employees in companies.items():
        print(company)
        for employee in employees:
            print(f'-- {employee}')


if __name__ == '__main__':
    company_data = register_employees()
    print_companies(companies=company_data)
