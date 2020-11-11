#!/usr/bin/env python

# Portscanner with  banner grabbing
# Jean-Bernard Altidor

# call: script.py <ipaddress> 

import sys
from datetime import datetime
import socket

OpenPortList =[]
def scanport(addr):
    #Check which port are open on host
    for port in range(1,1024):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setdefaulttimeout(1)
        result = socket_obj.connect_ex((addr,port))
        if result == 0:
            print ("Open socket detected: {}:{} \t-- Service: {} \t-- Hostname: {}".format(addr,port,socket.getservbyport(port),socket.gethostbyaddr(addr))) 
            OpenPortList.append(port)     
        s.close()

def banner_grabber(addr):
    #Try to get the banner
    for port in OpenPortList:
        print( "Attempting to get banner for port: ", port)
        bannergrabber = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(2)
        try:
            bannergrabber.connect((addr, port))
            bannergrabber.send('WhoAreYou\r\n')
            banner = bannergrabber.recv(100)
            bannergrabber.close()
            print( banner, "\n")
        except:
             print ("Cannot get banner ")