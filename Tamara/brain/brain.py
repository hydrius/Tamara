#!./bin/python

import pkgutil
from Tamara.sensors.wifi import Wifi
from queue import *
import datetime
from Tamara.brain.tts import GoogleTTS

class Brain():


    def __init__(self):

        self.__logger__("Brain initialised")
        self.logStatus = 0
        # Load TTS
        self.tts = GoogleTTS()

        # Checks to see if can speak
        # Stable since 29th March
        # Last tested on Lappy on 29th March

        #self.say("You. All. Turn. Me. On.")

        # Set variables
        self.awake = 1
        self.people = self.load_addressbook()
        self.ignore = self.load_ignorelist()
        #print(people)

        self.load_modules()


    def load_modules(self):

        # Add brain sensors - i.e functionality.
        self.q = Queue()

        #This will need sudo
        self.sensor = Wifi() # need to send address
        self.say("Wifi Sensor loaded")
        ret = self.sensor.connected(self.people, self.q)
        self.sensor.start()
        if ret == 0:
            self.say("Sudo Make Me A Sandwich")



    def get_sensor_data(self):
        #data = self.q.get_nowait()
        try:
            data = self.q.get_nowait()
            #print(data)
            return data

        except Exception as e:
            #print(e)
            #print("data is not being received")
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
            #self.__logger__("Sleeping")
        elif (now.hour < 21 and now.hour >=9) and self.awake == 0:
            self.__logger__("Good morning")
            self.say("Good Morning, coffee?")
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
