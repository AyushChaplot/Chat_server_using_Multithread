#!/usr/bin/env python
# coding: utf-8

# In[9]:


import socket
import threading


# In[15]:


def receiver():
    r =socket.socket(socket.SOCK_DGRAM,socket.AF_INET)
    r.bind(("192.168.43.181",4443))
    inbound = r.recvfrom(1024)
    print(inbound)


def sender():
    s = socket.socket(socket.SOCK_DGRAM,socket.AF_INET)
    s.sendto("hello from Win10".encode(),("192.168.43.12",5555))


t1 = threading.Thread(target=receiver)
t2 = threading.Thread(target=sender)

t1.start()
t2.start()


# In[ ]:





# In[ ]:




