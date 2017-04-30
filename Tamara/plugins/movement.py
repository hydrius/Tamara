import serial
import datetime
import random

class Movement():
    def __init__(self, Tamara):
        #self.data = data
        self.Tamara = Tamara
        # serial address of arduino
        # MOVE TO CONFIG ASAP
        address = "/dev/ttyUSB1"

        #initialise serial data
        try:
            self.ser = serial.Serial(address)
        except:
            #
            self.Tamara.__logger__("no port called " + address)

    def run(self):
        self.now = datetime.datetime.now().time()

        # serial in
        try:
            serin = self.ser.readline().decode("utf-8")
        except:
            serin = []

        print(serin)
        if "movement" in serin:
            diff = datetime.datetime.combine(datetime.date.min, self.now) - datetime.datetime.combine(datetime.date.min, self.prev)
            if diff > 300:
                if random.random() < 0.05:
                    self.Tamara.say("Hello!")
            self.prev = self.now



