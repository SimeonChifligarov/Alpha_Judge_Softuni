import unittest


class WorkerTests(unittest.TestCase):
    """
    This class tests the Worker class.
    """

    def setUp(self) -> None:
        self.worker = Worker(name='John', salary=1000, energy=5)

    def test_worker_is_initialized_correctly(self):
        self.assertEqual(self.worker.name, 'John')
        self.assertEqual(self.worker.salary, 1000)
        self.assertEqual(self.worker.energy, 5)
        self.assertEqual(self.worker.money, 0)

    def test_worker_energy_increases_after_rest(self):
        initial_energy = self.worker.energy
        self.worker.rest()
        self.assertEqual(self.worker.energy, initial_energy + 1)

    def test_worker_raises_exception_when_energy_zero_or_negative(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as context:
            self.worker.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

        self.worker.energy = -1
        with self.assertRaises(Exception) as context:
            self.worker.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_worker_money_increases_correctly_after_work(self):
        initial_money = self.worker.money
        self.worker.work()
        self.assertEqual(self.worker.money, initial_money + self.worker.salary)

    def test_worker_energy_decreases_after_work(self):
        initial_energy = self.worker.energy
        self.worker.work()
        self.assertEqual(self.worker.energy, initial_energy - 1)

    def test_worker_get_info_returns_correct_string(self):
        self.worker.money = 3000
        expected = 'John has saved 3000 money.'
        self.assertEqual(self.worker.get_info(), expected)


if __name__ == '__main__':
    unittest.main()
