import bike


class DockingStation:

    def __init__(self):
        self.docked_bikes = []
        self.capacity = 20
        self.Bike = bike.Bike
        for i in range(0, 20):
            self.docked_bikes.append(self.Bike(i + 1))

    def release_bike(self):
        if len(self.docked_bikes) <= 0:
            raise Exception("Error: No bikes available")
        else:
            bike = self.docked_bikes[0]
            self.docked_bikes.pop(0)
            return bike

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


