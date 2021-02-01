import unittest
import docking_station

DockingStation = docking_station.DockingStation


class TestDockingStation(unittest.TestCase):

    def test_docking_station_instance(self):
        docking_station = DockingStation()
        self.assertIsInstance(docking_station, DockingStation)

    def test_release_bike(self):
        docking_station = DockingStation()
        bike = docking_station.release_bike()
        # self.assertEqual(docking_station.release_bike(), "Bike released")
        self.assertEqual(bike.is_working(), True)