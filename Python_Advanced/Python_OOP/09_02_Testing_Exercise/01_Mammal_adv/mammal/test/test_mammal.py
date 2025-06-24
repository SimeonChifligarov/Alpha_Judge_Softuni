import unittest

from project.mammal import Mammal


class MammalTests(unittest.TestCase):
    """
    This class tests the Mammal class.
    """

    def setUp(self) -> None:
        self.mammal = Mammal(name='Leo', mammal_type='Lion', sound='Roar')

    def test_constructor_sets_all_attributes_correctly(self):
        self.assertEqual(self.mammal.name, 'Leo')
        self.assertEqual(self.mammal.type, 'Lion')
        self.assertEqual(self.mammal.sound, 'Roar')
        self.assertEqual(self.mammal._Mammal__kingdom, 'animals')

    def test_make_sound_returns_correct_string(self):
        expected = 'Leo makes Roar'
        self.assertEqual(self.mammal.make_sound(), expected)

    def test_get_kingdom_returns_animals(self):
        self.assertEqual(self.mammal.get_kingdom(), 'animals')

    def test_info_returns_correct_string(self):
        expected = 'Leo is of type Lion'
        self.assertEqual(self.mammal.info(), expected)


if __name__ == '__main__':
    unittest.main()
