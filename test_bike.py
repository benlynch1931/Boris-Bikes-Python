import unittest
import bike

Bike = bike.Bike


class TestBike(unittest.TestCase):

    def test_bike_working(self):
        bike = Bike(1)
        self.assertIsInstance(bike, Bike)
        self.assertEqual(bike.is_working(), True)

    def test_bike_name(self):
        bike = Bike(1)
        self.assertEqual(bike.name(), 'Bike 1')