#!./bin/python

import pkgutil
from Tamara.brain.sensors.wifi import Wifi
from queue import *
import datetime
from Tamara.brain.tts import GoogleTTS

class Brain():


    def __init__(self):

        self.__logger__("Brain initialised")
        self.logStatus = 0
        # Load TTS
        self.tts = GoogleTTS() 

        # Set variables
        self.awake = 1
        people = self.load_addressbook()
        ignore = self.load_ignorelist()
        #print(people)

        # Add brain sensors - i.e functionality.
        self.q = Queue()
        self.sensor = Wifi(people, self.q) # need to send address
        self.sensor.start()

    def get_sensor_data(self):
        try:
            data = self.q.get_nowait()
            return data
        except:
            pass

    def say(self, speech):
        self.tts.say(speech, "en") 

    def play(self, filename):
        self.tts.play(filename)

    def isAwake(self):
        now = datetime.datetime.now().time()

        if (now.hour >= 21 or now.hour < 9) and self.awake == 1:
            self.__logger__("Turning off")
            self.say("Good. night. sluts")
            self.awake = 0
        elif now.hour >= 21 or now.hour < 9:
            self.awake = 0 #redundant
            self.__logger__("Sleeping")
        elif (now.hour < 21 and now.hour >=9) and self.awake == 0:
            self.__logger__("Good morning")
            self.play("Good Morning, coffee?")
            self.awake = 1
        elif now.hour < 21 and now.hour >= 9:
            self.awake = 1 #redundant
            return True


    def __logger__(self, string, verbose=False):

        """
        Prints to file or stdout depending on Verbosity
        Verbose is always True
        """
        verbose = True
        if verbose:
            print(string)

        with open("log", "w+") as file: # change to append (a) when previous runs matter
            file.write("> %s\n" % string)

    def load_addressbook(self):
        addr = []
        with open("addressbook") as f:
            temp = f.readlines()
            for line in temp:
                addr.append(line.split())

            #for i, line in enumerate(addr):
            #    #append 0 for offline
            #    addr[i].append("0")

             #   #append time
             #   addr[i].append(datetime.datetime.now().time())
             #   addr[i].append(datetime.datetime.now().time()) 


        return addr

    def load_ignorelist(self):
        addr = []
        with open("ignorelist") as f:
            temp = f.readlines()
            for line in temp:
                addr.append(line.split())

        return addr



if __name__ == "__main__":
    b = Brain()
