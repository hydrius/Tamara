from Tamara.brain.brain import Brain
import threading
import copy
from queue import *
import time


# List of sensors
from Tamara.sensors.wifi import Wifi

# List of plugins
from Tamara.plugins.greetings import Greetings
from Tamara.plugins.clock import Clock
from Tamara.plugins.movement import Movement
from Tamara.plugins.ISS import SpaceStationNotifier

###############################################################################
#
#   To Do
#   - Add settings file
#   
#
###############################################################################


class Tamara(object):
    def __init__(self):
        self.Tamara = Brain()
        self.run()

    def run(self):
        """ 
        Jasper has this function direct to class Conversation to handle say events
        """

        # Set up modules for initialisation
        self.Tamara.__logger__("Setting up Modules")
        self.setup()

        # Check to see if awake.
        # TODO: Add time awake settings
        printOnce = 0
        while True:
            if printOnce == 0:
                self.Tamara.__logger__("Running Modules")
                printOnce = 1

            if self.Tamara.isAwake():
                # return sensor data. 
                data = self.Tamara.get_sensor_data()
                self.modules(data)

            time.sleep(1)
            #else:
            #    self.Tamara.__logger__("Sleeping")

    def setup(self):
        """
        initialise plugins go here up modules
        """
        self.clock = Clock(self.Tamara)
        self.greetings = Greetings(self.Tamara)
        self.Arduino = Movement(self.Tamara)
        self.SpaceStation = SpaceStationNotifier(self.Tamara)

    def modules(self, data):
        """
        After importing modules, simply send data to
        relevent module functions
        """
        self.greetings.run(data)
        self.clock.run(data)
        self.Arduino.run()
        self.SpaceStation.run()

if __name__ == "__main__":

    # Check Network
    #begin
    main()
    #app.run



