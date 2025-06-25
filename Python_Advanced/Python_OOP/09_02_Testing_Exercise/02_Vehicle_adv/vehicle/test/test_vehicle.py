import unittest

from project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):
    """
    This class tests the Vehicle class.
    """

    def setUp(self) -> None:
        self.vehicle = Vehicle(fuel=100.0, horse_power=150.0)

    def test_constructor_sets_all_attributes_correctly(self):
        self.assertEqual(self.vehicle.fuel, 100.0)
        self.assertEqual(self.vehicle.capacity, 100.0)
        self.assertEqual(self.vehicle.horse_power, 150.0)
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_reduces_fuel_correctly(self):
        self.vehicle.drive(10)
        expected_fuel = 100.0 - (Vehicle.DEFAULT_FUEL_CONSUMPTION * 10)
        self.assertEqual(self.vehicle.fuel, expected_fuel)

    def test_drive_raises_exception_when_not_enough_fuel(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(1000)
        self.assertEqual(str(context.exception), 'Not enough fuel')

    def test_refuel_increases_fuel_correctly(self):
        self.vehicle.drive(10)
        fuel_after_drive = self.vehicle.fuel
        self.vehicle.refuel(5)
        self.assertEqual(self.vehicle.fuel, fuel_after_drive + 5)

    def test_refuel_raises_exception_when_too_much_fuel(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(1)
        self.assertEqual(str(context.exception), 'Too much fuel')

    def test_str_returns_correct_string(self):
        expected = f'The vehicle has 150.0 horse power with 100.0 fuel left and {Vehicle.DEFAULT_FUEL_CONSUMPTION} fuel consumption'
        self.assertEqual(str(self.vehicle), expected)


if __name__ == '__main__':
    unittest.main()
