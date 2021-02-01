import bike


class DockingStation:

    def __init__(self):
        self.Bike = bike.Bike

    def release_bike(self):
        # return "Bike released"
        return self.Bike()
