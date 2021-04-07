# chat_server_using_UPD and Multithreading 
#User:2

import socket
import threading

def receiver():
    r =socket.socket(socket.SOCK_DGRAM,socket.AF_INET)
    r.bind(("192.168.43.12",5555))
    inbound = r.recvfrom(1024)
    print(inbound)


def sender():
    s = socket.socket(socket.SOCK_DGRAM,socket.AF_INET)
    s.sendto("hello from RHEL_arth".encode(),("192.168.43.181",4444))


t1 = threading.Thread(target=receiver)
t2 = threading.Thread(target=sender)

t1.start()
t2.start()
