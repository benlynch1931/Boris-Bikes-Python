import unittest
import bike

Bike = bike.Bike


class TestBike(unittest.TestCase):

    def test_bike_working(self):
        bike = Bike()
        self.assertIsInstance(bike, Bike)