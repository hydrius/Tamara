import datetime


class Greetings():

    def __init__(self, Tamara):
        self.Tamara = Tamara
        #self.Tamara.__logger__("Greetings is online")

    def run(self, data):
        self.addressbook = data
        if self.addressbook == None:
            self.addressbook = {}
        #try:
        for key, data in self.addressbook.items():
            #print(key,data)
            if "history" in self.addressbook[key]:
                time_b = self.addressbook[key]["history"][-1][-1]
                time_a = self.addressbook[key]["start"]

                # diff(time_a - time_b)
                diff = (datetime.datetime.combine(datetime.date.min, time_a) - datetime.datetime.combine(datetime.date.min, time_b)).total_seconds()
                print(key)
                print(diff)
                print(self.addressbook[key]["status"])
                if diff > 1200 and self.addressbook[key]["status"] == "1":
                    self.action(key)
            #except:
            #    pass
        #except:
        #    self.Tamara.__logger__("Data is likely None: sudo or internet issue")

    def action(self, name):
        speak = True
        filename = ""
        if name == "Master":
            self.Tamara.say("Welcome Home Master")
            filename = "/home/alarm/Tamara/Tamara/media/starwars.mp3"
        elif name == "Susan":
            self.Tamara.say("The wife is home")
            filename = "/home/alarm/Tamara/Tamara/media/tardis.mp3"
        elif name == "Dave":
            filename = "/home/alarm/Tamara/Tamara/media/spanishFlea.mp3"
        elif name == "Sadie":
            speak = False
            self.Tamara.say("Oh no... Sadie is here... This means Sangria time!")
        elif name == "Morgan":
            speak = False
            self.Tamara.say("Morgan is here. Time to get wrecked, cunt")
        elif name == "Aaron":
            filename = "/home/alarm/Tamara/Tamara/media/megaman.mp3"

        if speak:
            print(filename)
            self.Tamara.play(filename)
