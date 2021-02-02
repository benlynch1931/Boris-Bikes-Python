import bike


class DockingStation:

    def __init__(self, capacity = 20):
        self.docked_bikes = []
        self.capacity = capacity
        self.Bike = bike.Bike
        for i in range(0, self.capacity):
            self.docked_bikes.append(self.Bike(i + 1))

    def release_bike(self):
        self.__is_empty()
        bike = self.__get_bike()
        return bike

    def dock_bike(self, bike):
        self.__is_full()
        self.docked_bikes.append(bike)
        return self.docked_bikes

    def view_bikes(self):
        bike_array = []
        for i in range(0, len(self.docked_bikes)):
            condition = self.__bike_condition(self.docked_bikes[i])
            bike_array.append('{0} - {1}'.format(self.docked_bikes[i].name(), condition))
        return bike_array

    def __get_bike(self):
        bike = self.docked_bikes[0]
        self.docked_bikes.pop(0)
        return bike

    def __bike_condition(self, docked_bike):
        condition = "Working" if docked_bike.is_working else "Broken"
        return condition

    def __is_full(self):
        if len(self.docked_bikes) >= self.capacity:
            raise Exception("Error: Docking station as maximum capacity")
        else:
            return None

    def __is_empty(self):
        if len(self.docked_bikes) <= 0:
            raise Exception("Error: No bikes available")
        else:
            return None

