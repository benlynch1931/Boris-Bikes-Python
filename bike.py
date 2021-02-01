class Bike:

    def __init__(self, number):
        self.working = True
        self.bike_name = 'Bike {0}'.format(number)

    def is_working(self):
        return self.working

    def name(self):
        return self.bike_name