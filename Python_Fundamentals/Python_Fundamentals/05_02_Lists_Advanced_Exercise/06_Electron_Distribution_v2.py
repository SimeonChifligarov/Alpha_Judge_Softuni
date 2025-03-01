def distribute_electrons(electrons: int) -> list[int]:
    shells = []
    shell_position = 1

    while electrons > 0:
        max_electrons = 2 * (shell_position ** 2)
        electrons_in_shell = min(electrons, max_electrons)
        shells.append(electrons_in_shell)
        electrons -= electrons_in_shell
        shell_position += 1

    return shells


if __name__ == '__main__':
    total_electrons = int(input())
    print(distribute_electrons(electrons=total_electrons))
