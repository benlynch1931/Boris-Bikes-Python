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

    def view_bikes(self):
        bike_array = []
        for i in range(0, len(self.docked_bikes)):
            if self.docked_bikes[i].is_working:
                condition = "Working"
            else:
                condition = "Broken"
            bike_array.append('{0} - {1}'.format(self.docked_bikes[i].name(), condition))
        return bike_array
