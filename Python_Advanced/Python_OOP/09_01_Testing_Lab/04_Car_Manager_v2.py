import unittest


class CarTests(unittest.TestCase):
    """
    This class tests the Car class.
    """

    def setUp(self) -> None:
        self.car = Car(make='Toyota', model='Corolla', fuel_consumption=5, fuel_capacity=50)

    def test_constructor_sets_all_attributes_correctly(self):
        self.assertEqual(self.car.make, 'Toyota')
        self.assertEqual(self.car.model, 'Corolla')
        self.assertEqual(self.car.fuel_consumption, 5)
        self.assertEqual(self.car.fuel_capacity, 50)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_make_setter_raises_exception_when_empty(self):
        with self.assertRaises(Exception) as context:
            self.car.make = ''
        self.assertEqual(str(context.exception), 'Make cannot be null or empty!')

    def test_model_setter_raises_exception_when_empty(self):
        with self.assertRaises(Exception) as context:
            self.car.model = ''
        self.assertEqual(str(context.exception), 'Model cannot be null or empty!')

    def test_fuel_consumption_setter_raises_exception_when_zero_or_negative(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = 0
        self.assertEqual(str(context.exception), 'Fuel consumption cannot be zero or negative!')

        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = -5
        self.assertEqual(str(context.exception), 'Fuel consumption cannot be zero or negative!')

    def test_fuel_capacity_setter_raises_exception_when_zero_or_negative(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = 0
        self.assertEqual(str(context.exception), 'Fuel capacity cannot be zero or negative!')

        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = -10
        self.assertEqual(str(context.exception), 'Fuel capacity cannot be zero or negative!')

    def test_fuel_amount_setter_raises_exception_when_negative(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -1
        self.assertEqual(str(context.exception), 'Fuel amount cannot be negative!')

    def test_refuel_increases_fuel_amount_correctly(self):
        self.car.refuel(20)
        self.assertEqual(self.car.fuel_amount, 20)

    def test_refuel_cannot_exceed_capacity(self):
        self.car.refuel(100)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_refuel_raises_exception_when_zero_or_negative(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(0)
        self.assertEqual(str(context.exception), 'Fuel amount cannot be zero or negative!')

        with self.assertRaises(Exception) as context:
            self.car.refuel(-10)
        self.assertEqual(str(context.exception), 'Fuel amount cannot be zero or negative!')

    def test_drive_reduces_fuel_amount_correctly(self):
        self.car.refuel(50)
        self.car.drive(100)
        expected_fuel = 50 - (100 / 100 * 5)
        self.assertEqual(self.car.fuel_amount, expected_fuel)

    def test_drive_raises_exception_when_not_enough_fuel(self):
        self.car.refuel(1)
        with self.assertRaises(Exception) as context:
            self.car.drive(100)
        self.assertEqual(str(context.exception), "You don't have enough fuel to drive!")


if __name__ == '__main__':
    unittest.main()
