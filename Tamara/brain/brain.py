#!./bin/python

import pkgutil
from Tamara.sensors.wifi import Wifi
#from Tamara.sensors.listen import Listen
from queue import *
import datetime
from Tamara.brain.tts import GoogleTTS

class Brain():

    def __init__(self):

        # File Path
        self.addressbook_path = "addressbook"
        self.ignore_path = "ignorelist"

        self.__logger__("Brain initialised\n")
        self.logStatus = 0
        # Load TTS
        self.tts = GoogleTTS()
        #self.stt = GoogleSTT()
        # Checks to see if can speak
        # Stable since 29th March
        # Last tested on Lappy on 29th March

        self.say("You. All. Turn. Me. On.")

        # Set variables
        self.awake = 1

        self.people = self.load_addressbook()
        self.ignore = self.load_ignorelist()
        #print(people)

        self.load_modules()
        

    def load_modules(self):

        # Add brain sensors - i.e functionality.
        self.q_wifi = Queue()
        self.q_listen = Queue()

        #This will need sudo
        self.wifi = Wifi() # need to send address
        #self.listen = Listen()

        ret = self.wifi.connected(self.people, self.q_wifi)
        if ret == 0:
            self.__logger__(f"Not sudo or connected to the internet?") 
            self.say("Sudo Make Me A Sandwich")
        else:
            self.__logger__(f"Wifi sensor connected successfully:result is {ret} == 1")

        self.wifi.start()
        #self.listen.start()


    def get_sensor_data(self):
        #data = self.q.get_nowait()
        try:
            data = self.q_wifi.get_nowait()
            return data

        except Exception as e:
            pass

            # The below will trigger when threads are not synced
            #self.__logger__("{e}")
            #self.__logger__(f"failed to receive data")/

    def say(self, speech):
        self.__logger__(f"saying > {speech}")
        self.tts.say(speech, "en")

    def play(self, filename):
        self.tts.play(filename)

    def isAwake(self):
        now = datetime.datetime.now().time()

        if now.minute == 0:
            self.__logger(f"{now.hour}:{now.minute}")

        if (now.hour >= 21 or now.hour < 9) and self.awake == 1:
            self.__logger__("Good Night Sluts")
            self.say("Good night sluts")
            self.awake = 0
        elif now.hour >= 21 or now.hour < 9:
            self.awake = 0 #redundant
            #self.__logger__("Sleeping")
        elif (now.hour < 21 and now.hour >=9) and self.awake == 0:
            self.__logger__("Good morning everyone")
            self.say("Good Morning, coffee?")
            self.awake = 1
        elif now.hour < 21 and now.hour >= 9:
            self.awake = 1 #redundant
            return True


    def __logger__(self, string, verbose=True):

        """
        Prints to file or stdout depending on Verbosity
        Verbose is always True
        """
        now = datetime.datetime.now()
        time = f"{now.hour}:{now.minute}"

        strlog = f"{time} > {string}"

        verbose = True
        if verbose:
            print(f"{strlog}")

        with open("log", "a+") as file: # change to append (a) when previous runs matter
            file.write(f"{strlog}\n")

    def load_addressbook(self):
        addr = []
        with open(self.addressbook_path) as f:
            temp = f.readlines()
            for line in temp:
                addr.append(line.split())
        self.__logger__("Address Book")
        self.__logger__("------------")
        for line in addr:
            self.__logger__(line)
        return addr

    def load_ignorelist(self):
        addr = []
        with open(self.ignore_path) as f:
            temp = f.readlines()
            for line in temp:
                addr.append(line.split())

        self.__logger__("IgnoreList")
        self.__logger__("----------")
        for line in addr:
            self.__logger__(line)

        return addr



if __name__ == "__main__":
    b = Brain()
