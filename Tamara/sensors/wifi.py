from threading import *
import datetime
import os
import subprocess
import sys
import time
class Wifi(Thread):

    def __init__(self, address, q, data={}):
        super(Wifi, self).__init__()


        self.q = q
        self.addressbook = address
        self.data = data

        # temp solution until pickle up and running
        self.data = {"online": [],
                    }

    def run(self):

        # Run Forever!!!!
        while True:
            i = 0


            p = subprocess.Popen("arp-scan -l", stdout=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()
            p_status = p.wait()

            # Search for names
            for name, addr in self.addressbook:
                now = datetime.datetime.now().time()
                if name not in self.data:
                    self.new_user(name, addr, now)

                if addr in output.decode("utf-8") and self.data[name]["status"] == "0":

                    if name not in self.data["online"]:
                        print(name, "is online")
                        self.data["online"].append(name)

                        self.data[name]["finish"] = now
                        self.data[name]["start"] = now
                        self.data[name]["status"] = "1"

                elif addr in output.decode("utf-8"):
                    #print(name, "is still online")
                    self.data[name]["finish"] = now
                    self.data[name]["status"] = "2"


                elif not addr in output.decode("utf-8") and (self.data[name]["status"] == "1" or self.data[name]["status"] == "2"):
                    #User has disconnected
                    if name in self.data["online"]:
                        print(name,"disconnected")
                        self.data["online"].remove(name)
                        self.data[name]["status"] = "0"

                        start = self.data[name]["start"]
                        finish = self.data[name]["finish"] 

                        self.data[name]["history"].append([start,finish])
                i=+1

            self.q.put(self.data)
            time.sleep(2)

    def new_user(self, name, address, now):
        print(f"adding new user {name}")
        self.data[name] = {"mac": address,
                           "status": "0", # 0 offline; 1 online; 2; already connected
                           "online": True,
                           "start": now,
                           "finish": now,
                           "history": [[now,now]],
                           "session": 0,
                           }

    def clean(self):
        for key, data in self.data.items():
            try:
                if self.data[key]["start"] > 100:
                    print("delete the last 90 values")
                    # Delete last 90 values 
                    # But somehow get total time acrued.

            except:
                pass
