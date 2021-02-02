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
        docking_station.release_bike()
        self.assertIsInstance(docking_station.dock_bike(Bike(1))[19], Bike)

    def test_view_bikes(self):
        docking_station = DockingStation()
        self.assertEqual(docking_station.view_bikes()[0], 'Bike 1 - Working')
        self.assertEqual(docking_station.view_bikes()[10], 'Bike 11 - Working')
        self.assertEqual(docking_station.view_bikes()[19], 'Bike 20 - Working')

    def test_bike_capacity(self):
        docking_station = DockingStation()
        for i in range(0, 20):
            docking_station.release_bike()
        with self.assertRaises(Exception) as context:
            docking_station.release_bike()

        self.assertTrue('Error: No bikes available' in context.exception)