import unittest
import docking_station
import bike

DockingStation = docking_station.DockingStation
Bike = bike.Bike


class TestDockingStation(unittest.TestCase):

    def test_docking_station_instance(self):
        docking_station = DockingStation()
        self.assertIsInstance(docking_station, DockingStation)

    def test_release_bike(self):
        docking_station = DockingStation()
        bike = docking_station.release_bike()
        # self.assertEqual(docking_station.release_bike(), "Bike released")
        self.assertEqual(bike.is_working(), True)

    def test_dock_bike(self):
        docking_station = DockingStation()
        self.assertIsInstance(docking_station.dock_bike(Bike(1))[0], Bike)

    def test_view_bikes(self):
        docking_station = DockingStation()
        docking_station.dock_bike(Bike(1))
        self.assertEqual(docking_station.view_bikes(), ['Bike 1 - Working'])