import datetime

class Greetings():

    def __init__(self, Tamara):
        self.Tamara = Tamara
        print("WHY ARE YOU REPEATING")
    def run(self, data):

        self.addressbook = data[0]
        self.num = data[1]
        self.online = data[2]

        for i, person in enumerate(self.addressbook):
            time_a = self.addressbook[i][3]
            time_b = self.addressbook[i][4]

            diff = (datetime.datetime.combine(datetime.date.min, person[4]) - datetime.datetime.combine(datetime.date.min, person[3])).total_seconds()

            if diff > 300:
                self.action(person[0])

    def action(self, name):
        speak = True
        filename = ""
        if name == "Master":
            self.Tamara.say("Welcome Home Master")
            filename = "media/starwars.mp3"
        elif name == "Susan":
            self.Tamara.say("The wife is home")
            filename = "media/tardis.mp3"
        elif name == "Dave":
            filename = "media/spanishFlea.mp3"
        elif name == "Sadie":
            speak = False
            self.Tamara.say("Oh no... Sadie is here... This means Sangria time!")
        elif name == "Morgan":
            speak = False
            self.Tamara.say("Morgan is here. Time to get wrecked, cunt")
        elif name == "Aaron":
            filename = "media/megaman.mp3"

        if speak:
            print(filename)
            self.Tamara.play(filename)
