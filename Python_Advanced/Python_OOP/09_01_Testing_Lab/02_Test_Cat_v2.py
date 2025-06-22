import unittest


class CatTests(unittest.TestCase):
    """
    This class tests the Cat class.
    """

    def setUp(self) -> None:
        self.cat = Cat(name='Whiskers')

    def test_cat_size_increases_after_eating(self):
        initial_size = self.cat.size
        self.cat.eat()
        self.assertEqual(self.cat.size, initial_size + 1)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_cannot_eat_if_already_fed_raises_error(self):
        self.cat.eat()
        with self.assertRaises(Exception) as context:
            self.cat.eat()
        self.assertEqual(str(context.exception), 'Already fed.')

    def test_cat_cannot_sleep_if_not_fed_raises_error(self):
        with self.assertRaises(Exception) as context:
            self.cat.sleep()
        self.assertEqual(str(context.exception), 'Cannot sleep while hungry')

    def test_cat_is_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
