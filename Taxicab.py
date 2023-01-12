# Author: Drew Cochran
# Date: 27OCT21
# Description: A class called taxicab that takes in x and y coordinates and odometer readings, and calculates the total odometer
#           readings based on movement.


class Taxicab:
    """
    Taxicab object that uses x and y coordinates to calculate movement and tracks the movement using an odometer reading.
    """

    def __init__(self, x, y):
        """
        Creates a system for movement using standard x and y coordinates with an odometer reading.
        :param x:
        :param y:
        :param odometer:
        """

        odometer = 0
        self._x = x
        self._y = y
        self._odometer = odometer

    def get_x_coord(self):
        """
        Returns the x coordinate value.
        :return _x :
        """
        return self._x

    def get_y_coord(self):
        """
        Returns the y coordinate value.
        :return _y :
        """
        return self._y

    def get_odometer(self):
        """
        Returns the odometer value.
        :return odometer:
        """
        return self._odometer

    def move_x(self, amount):
        """
        Takes in the value of x movement, changes the position of the x coordinate appropriately,
         and adds to the odometer
        :param amount:
        :return:
        """
        if amount > 0:
            self._x += abs(amount)
        else:
            self._x -= abs(amount)

        self._odometer += abs(amount)

    def move_y(self, amount):
        """
          Takes in the value of y movement, changes the position of the y coordinate appropriately,
         and adds to the odometer
        :param amount:
        :return:
        """
        if amount > 0:
            self._y += abs(amount)
        else:
            self._y -= abs(amount)

        self._odometer += abs(amount)