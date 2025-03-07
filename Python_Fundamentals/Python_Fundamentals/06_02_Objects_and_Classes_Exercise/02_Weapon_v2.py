class Weapon:
    """
    Represents a weapon with a limited number of bullets and shooting functionality.
    """

    def __init__(self, bullets: int) -> None:
        self.bullets = bullets

    def shoot(self) -> str:
        if self.bullets > 0:
            self.bullets -= 1
            return 'shooting...'
        return 'no bullets left'

    def __repr__(self) -> str:
        return f'Remaining bullets: {self.bullets}'

# if __name__ == '__main__':
#     weapon_instance = Weapon(bullets=int(input()))
#
#     for _ in range(int(input())):
#         print(weapon_instance.shoot())
#
#     print(weapon_instance)
