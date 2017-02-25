import datetime
import random

class Clock():
    def __init__(self, Tamara):
        self.Tamara = Tamara
        self.hasRun = 0
        self.last = 0
    def run(self):
        now = datetime.datetime.now().time()
        if now.hour == 4 and now.minute == 20:
            self.Tamara.say("Hey everyone... Happy 4 20")

    def sayings(self):
        lines = ["Happy four twenty", 
                 "Hey everyone.... Happy four twenty", 
                 "It is four twenty... cunt",
                 "Cunt",
                 "four twenty"]

        secure_random = random.SystemRandom()
        return secure_random.choice(lines)
 
