import serial


class Movement():
    def __init__(self, Tamara):
        #self.data = data
        self.Tamara = Tamara
        # serial address of arduino
        address = "/dev/ttyUSB1"

        #initialise serial data
        self.ser = serial.Serial(address)

    def run(self):

        # serial in
        serin = self.ser.readline().decode("utf-8")

        print(serin)
        if "movement" in serin:
            self.Tamara.say("movement")



