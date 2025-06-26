import unittest

from project.hero import Hero


class HeroTests(unittest.TestCase):
    """
    This class tests the Hero class.
    """

    def setUp(self) -> None:
        self.hero = Hero(username='Hero1', level=5, health=100.0, damage=20.0)
        self.enemy = Hero(username='Enemy', level=5, health=100.0, damage=15.0)

    def test_constructor_sets_all_attributes_correctly(self):
        self.assertEqual(self.hero.username, 'Hero1')
        self.assertEqual(self.hero.level, 5)
        self.assertEqual(self.hero.health, 100.0)
        self.assertEqual(self.hero.damage, 20.0)

    def test_battle_raises_exception_when_fighting_yourself(self):
        with self.assertRaises(Exception) as context:
            self.hero.battle(self.hero)
        self.assertEqual(str(context.exception), 'You cannot fight yourself')

    def test_battle_raises_value_error_when_hero_health_is_zero_or_negative(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.enemy)
        self.assertEqual(str(context.exception), 'Your health is lower than or equal to 0. You need to rest')

        self.hero.health = -10
        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.enemy)
        self.assertEqual(str(context.exception), 'Your health is lower than or equal to 0. You need to rest')

    def test_battle_raises_value_error_when_enemy_health_is_zero_or_negative(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.enemy)
        self.assertEqual(str(context.exception), 'You cannot fight Enemy. He needs to rest')

        self.enemy.health = -20
        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.enemy)
        self.assertEqual(str(context.exception), 'You cannot fight Enemy. He needs to rest')

    def test_battle_returns_draw_when_both_healths_drop_to_zero_or_below(self):
        self.hero.health = 100
        self.hero.damage = 20
        self.enemy.health = 100
        self.enemy.damage = 20
        self.hero.level = 5
        self.enemy.level = 5
        result = self.hero.battle(self.enemy)
        self.assertEqual(result, 'Draw')

    def test_battle_returns_you_win_and_updates_hero_stats_correctly(self):
        self.enemy.health = 10
        self.enemy.damage = 1
        result = self.hero.battle(self.enemy)
        self.assertEqual(result, 'You win')
        self.assertEqual(self.hero.level, 6)
        self.assertEqual(self.hero.health, 100.0 - (1 * 5) + 5)
        self.assertEqual(self.hero.damage, 25.0)

    def test_battle_returns_you_lose_and_updates_enemy_stats_correctly(self):
        self.hero.health = 10
        self.hero.damage = 1
        result = self.hero.battle(self.enemy)
        self.assertEqual(result, 'You lose')
        self.assertEqual(self.enemy.level, 6)
        self.assertEqual(self.enemy.health, 100.0 - (1 * 5) + 5)
        self.assertEqual(self.enemy.damage, 20.0)

    def test_str_returns_correct_format(self):
        expected = 'Hero Hero1: 5 lvl\nHealth: 100.0\nDamage: 20.0\n'
        self.assertEqual(str(self.hero), expected)


if __name__ == '__main__':
    unittest.main()
