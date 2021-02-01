import unittest
import boris_bikes

DockingStation = boris_bikes.DockingStation

class TestBorisBikes(unittest.TestCase):

    def test_docking_station_instance(self):
        docking_station = DockingStation()
        self.assertIsInstance(docking_station, DockingStation)
    # def test_release_bike(self):
