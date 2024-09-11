import socket


UDP_PORT = 5005
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


def ReciveData(UDP_IP):

    #UDP_IP = input("What Is The IP of the user that you want to recive data from him: ")
    sock.bind((UDP_IP,UDP_PORT))
    while True:
        data, addr = sock.recvfrom(1024) # buffer size 1024 bytes
        data = str(data)
        data = data.replace("'","")
        data = data.replace("b","")
        print(data)

