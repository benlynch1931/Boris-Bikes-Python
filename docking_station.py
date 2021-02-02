import bike


class DockingStation:

    def __init__(self):
        self.docked_bikes = []
        self.Bike = bike.Bike

    def release_bike(self):
        # return "Bike released"
        return self.Bike()

    def dock_bike(self, bike):
        self.docked_bikes.append(bike)
        return self.docked_bikes
