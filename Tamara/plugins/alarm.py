import serial


class AlarmPy():
    def __init__(self, data):
        self.data = data

        # serial address of arduino
        address = "/dev/ttyUSB0"

        #initialise serial data
        self.ser = serial.Serial(address)

    def run(self):

        # serial in
        serin = self.ser.readline().decode("utf-8")
        serin.split()

        if serin[0] == 1 and len(self.data["online"]) == 0:
            print("Intruder")


