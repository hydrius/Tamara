from Tamara.brain.brain import Brain
import threading
import copy
from queue import *
import time


# List of sensors
from Tamara.brain.sensors.wifi import Wifi

# List of plugins
from Tamara.brain.plugins.greetings import Greetings
from Tamara.brain.plugins.clock import Clock
from Tamara.brain.plugins.movement import Movement


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
        self.Tamara.say("Cash me outside. How. about. that!")
        self.run()

    def run(self):
        """ 
        Jasper has this function direct to class Conversation to handle say events
        """

        # Set up modules for initialisation
        self.Tamara.__logger__("Set up Modules")
        self.setup()

        # Check to see if awake.
        # TODO: Add time awake settings
        timesPrinted = 0
        while True:
            if timesPrinted == 0:
                self.Tamara.__logger__("Running Modules")
                timesPrinted = 1

            if self.Tamara.isAwake():
                # return sensor data. 
                data = self.Tamara.get_sensor_data()
                if data is not None:
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

    def modules(self, data):
        """
        After importing modules, simply send data to
        relevent module functions
        """
        
        self.greetings.run(data)
        self.clock.run(data)
        self.Arduino.run()
if __name__ == "__main__":

    # Check Network
    #begin
    main()
    #app.run



