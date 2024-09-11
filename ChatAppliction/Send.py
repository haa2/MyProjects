import socket

UDP_PORT = 5005

def TransmitData(Context):

    UDP_IP = input("What Is The IP of the user that you want to send it to: ")

    Context = bytes(Context,'utf-8')

    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #UDP Socket

    sock.sendto(Context, (UDP_IP,UDP_PORT))

