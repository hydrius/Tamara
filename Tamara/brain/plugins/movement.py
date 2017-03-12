import serial


class Movement():
    def __init__(self, data, Tamara):
        self.data = data
        self.Tamara = Tamara
        # serial address of arduino
        address = "/dev/ttyUSB0"

        #initialise serial data
        self.ser = serial.Serial(address)

    def run(self):

        # serial in
        serin = self.ser.readline().decode("utf-8")

        print(serin)
        if serin == "movement":
            self.Tamara.say("movement")



