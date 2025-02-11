def fire_extinguishing_simulation(fire_data: str, water: int) -> None:
    """
    Simulates the fire extinguishing process based on fire levels and available water.
    """
    fires = fire_data.split('#')
    total_effort = 0
    total_fire = 0
    extinguished_cells = []

    for fire in fires:
        fire_type, value = fire.split(' = ')
        value = int(value)

        valid = (
            (fire_type == 'High' and 81 <= value <= 125) or
            (fire_type == 'Medium' and 51 <= value <= 80) or
            (fire_type == 'Low' and 1 <= value <= 50)
        )

        if valid and water >= value:
            water -= value
            total_fire += value
            effort = value * 0.25
            total_effort += effort
            extinguished_cells.append(value)

    print('Cells:')
    for cell in extinguished_cells:
        print(f' - {cell}')
    print(f'Effort: {total_effort:.2f}')
    print(f'Total Fire: {total_fire}')


if __name__ == '__main__':
    fire_input = input()
    water_input = int(input())
    fire_extinguishing_simulation(fire_data=fire_input, water=water_input)
