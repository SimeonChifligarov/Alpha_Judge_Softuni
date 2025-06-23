import unittest


class IntegerListTests(unittest.TestCase):
    """
    This class tests the IntegerList class.
    """

    def setUp(self) -> None:
        self.integer_list = IntegerList(1, 2, 3, 4, 5)

    def test_constructor_stores_only_integers(self):
        integer_list = IntegerList(1, '2', 3.5, 4)
        self.assertEqual(integer_list.get_data(), [1, 4])

    def test_add_integer_adds_correctly(self):
        result = self.integer_list.add(10)
        self.assertEqual(result, [1, 2, 3, 4, 5, 10])

    def test_add_non_integer_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.integer_list.add('10')
        self.assertEqual(str(context.exception), 'Element is not Integer')

    def test_remove_index_removes_and_returns_correct_element(self):
        removed = self.integer_list.remove_index(2)
        self.assertEqual(removed, 3)
        self.assertEqual(self.integer_list.get_data(), [1, 2, 4, 5])

    def test_remove_index_out_of_range_raises_index_error(self):
        with self.assertRaises(IndexError) as context:
            self.integer_list.remove_index(10)
        self.assertEqual(str(context.exception), 'Index is out of range')

    def test_get_returns_correct_element(self):
        element = self.integer_list.get(1)
        self.assertEqual(element, 2)

    def test_get_out_of_range_raises_index_error(self):
        with self.assertRaises(IndexError) as context:
            self.integer_list.get(5)
        self.assertEqual(str(context.exception), 'Index is out of range')

    def test_insert_integer_inserts_correctly(self):
        self.integer_list.insert(2, 99)
        self.assertEqual(self.integer_list.get_data(), [1, 2, 99, 3, 4, 5])

    def test_insert_index_out_of_range_raises_index_error(self):
        with self.assertRaises(IndexError) as context:
            self.integer_list.insert(10, 99)
        self.assertEqual(str(context.exception), 'Index is out of range')

    def test_insert_non_integer_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.integer_list.insert(1, '99')
        self.assertEqual(str(context.exception), 'Element is not Integer')

    def test_get_biggest_returns_biggest_element(self):
        self.assertEqual(self.integer_list.get_biggest(), 5)

    def test_get_index_returns_correct_index(self):
        self.assertEqual(self.integer_list.get_index(4), 3)


if __name__ == '__main__':
    unittest.main()
