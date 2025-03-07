class Weapon:
    def __init__(self, bullets: int):
        """Initializes the weapon with a given number of bullets."""
        self.bullets = bullets

    def shoot(self) -> str:
        """Shoots a bullet if available, otherwise returns a warning message."""
        if self.bullets > 0:
            self.bullets -= 1
            return 'shooting...'
        return 'no bullets left'

    def __repr__(self) -> str:
        """Returns a string representation of the remaining bullets."""
        return f'Remaining bullets: {self.bullets}'
