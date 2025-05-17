class Hero:
    """
    This class is for a hero character. It has a name and health value.

    Args:
        name (str): The name of the hero
        health (int): The current health of the hero
    """

    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health

    def defend(self, damage: int) -> str:
        """
        This method reduces health by the damage taken.
        If health drops to 0 or less, it sets health to 0 and tells that the hero was defeated.

        Args:
            damage (int): The damage to reduce

        Returns:
            str: Message if defeated, else empty string
        """
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            return f'{self.name} was defeated'
        return ''

    def heal(self, amount: int) -> None:
        """
        This method increases the hero's health by the given amount.

        Args:
            amount (int): The healing amount
        """
        self.health += amount

# if __name__ == '__main__':
#     hero_name = 'Archer'
#     hero_health = 100
#     hero_instance = Hero(name=hero_name, health=hero_health)
#     print(hero_instance.defend(damage=60))
#     print(hero_instance.defend(damage=50))
#     hero_instance.heal(amount=30)
#     print(hero_instance.health)
