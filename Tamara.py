#from brain.brain import tts

from brain.brain import Brain
import threading
import copy
from queue import *
from brain.sensors.wifi import Wifi
from brain.plugins.clock import Clock
import time
from brain.plugins.greetings import Greetings


class Tamara(object):
    def __init__(self):
        self.Tamara = Brain()
        self.run()

    def run(self):
        """ 
        Jasper has this function direct to class Conversation to handle say events
        """
        # Functionality
        if self.Tamara.isAwake():
            self.setup()
            while True:
                data = self.Tamara.get_sensor_data()
                if data is not None:
                    self.modules(data)


    def setup(self):
        self.clock = Clock(self.Tamara)
        self.greetings = Greetings(self.Tamara)

    def modules(self, data):
        """
        After importing modules, simply send data to
        relevent module functions
        """
        self.i_can_see(data)
        self.the_time_is(data)

    def i_can_see(self, data):
        x = 1
        #if data is not None:
        #    print(data)

    def the_time_is(self, data):
        """ 
        Clock is initiated and sent Brain() object and data before running
        """
        self.greetings.run(data)

if __name__ == "__main__":

    # Check Network
    #begin
    app = Tamara()
    #app.run



