

import Recive,Send

UDP_IP = input("What Is the User IP ")

while True:
    if Recive.ReciveData(UDP_IP):
        print(Recive.ReciveData(UDP_IP))
    else:
        Send.TransmitData(input("What Is the Context You Want to Send: "))
