from threading import *
import datetime
import os
import subprocess
import sys

class Wifi(Thread):

    def __init__(self, address, q):
        super(Wifi, self).__init__()
        self.q = q
        self.addressbook = address
        self.devicesConnected = 0
        self.online = []

    def run(self):
        i = 0
        while True:
            i = 0

            # Search for name
            for name, addr, status, previous, date in self.addressbook:
                now = datetime.datetime.now().time()
                p = subprocess.Popen("arp-scan -l | grep %s" % str(addr), stdout=subprocess.PIPE, shell=True)
                (output, err) = p.communicate()
                p_status = p.wait()

                if output and status == "0":
                    #User has connected
                    if name not in self.online:
                        print(name, addr)
                        self.online.append(name)
                        self.devicesConnected +=1
                    #print(date) 
                    self.addressbook[i][3] = self.addressbook[i][4]
                    self.addressbook[i][4] = now
                    self.addressbook[i][2] = "1"

                elif output:
                    self.addressbook[i][3] = self.addressbook[i][4] 
                    self.addressbook[i][4] = now

                elif not output and (status == "1" or status == "2"):
                    #User has disconnected
                    if name in self.online:
                        self.devicesConnected -=1
                        self.online.remove(name)
                    self.addressbook[i][2] = "0"
                i=+1
            data = (self.addressbook, self.devicesConnected, self.online)
            self.q.put(data)

