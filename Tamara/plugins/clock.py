import datetime
import random

class Clock():
    def __init__(self, Tamara):
        self.Tamara = Tamara
        self.hasRun = False
        self.Tamara.__logger__("Clock is online")

    def run(self, data):
        now = datetime.datetime.now().time()
        if now.hour == 16 and now.minute == 2:
            if not self.hasRun:
                time_str = now.strftime("%Y-%m-%d %H:%M:%S")
                self.Tamara.__logger__(f"{time_str}: 420"),
                self.Tamara.say(self.sayings())
                self.hasRun = True

        if now.hour < 10:
            self.hasRun = False

    def sayings(self):
        lines = ["Happy four twenty", 
                 "Hey everyone.... Happy four twenty", 
                 "It is four twenty... cunt",
                 "Cunt",
                 "four twenty"]

        secure_random = random.SystemRandom()
        return secure_random.choice(lines)
 
