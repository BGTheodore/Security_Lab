#!/usr/bin/env python

# Portscanner with  banner grabbing
# Jean-Bernard Altidor

# call: script.py <ipaddress> 

import sys
from datetime import datetime
import socket
import os
import csv

dicData = {}
data=[]
def scanport(addr):
    #Check which port are open on host
 try:
    for port in range(1,1024):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       # s.setdefaulttimeout(1)
        result = s.connect_ex((addr,port))
        if result == 0:
            data =[]
            banner = banner_grabber(addr,port)
            domain = socket.gethostbyaddr(addr)[0]
            service =str(socket.getservbyport(port))
            print ("Open socket detected: {}:{} \t-- Service: {} \t-- Hostname: {} \t--Banner: {}" .format(addr,port,service,domain, banner)) 
            data.append(str(addr)) 
            data.append(str(service))
            data.append(str(domain))
            data.append(str(banner))
            # opening the csv file in 'w+' mode 
            dicData[port] = data

  
 except socket.error:
     pass
 finally:
        s.close()

def banner_grabber(addr,port):
    #Try to get the banner
   
        print( "Attempting to get banner for port: ", port)
        bannergrabber = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #bannergrabber.setdefaulttimeout(2)
        try:
            bannergrabber.connect((addr, port))
            bannergrabber.send('WhoAreYou\r\n')
            banner = bannergrabber.recv(100)
            #bannergrabber.send('GET HTTP/1.1 \r\n')
            #bannergrabber.send('WhoAreYou\r\n')
           # banner = bannergrabber.recv(1024)
            bannergrabber.close()
            return banner
        except:
             return "Cannot get banner"



if __name__ == "__main__":
    addr = input('Enter the destination : ')
    scanport(addr)
    print(dicData)
    csv_columns = ['Port', 'IP', 'Service', 'Domain', 'Banner']
    with open('report.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=csv_columns)
        writer.writeheader()
        for key in dicData.keys():
            f.write("%s, %s, %s, %s, %s\n" % (key, dicData[key][0], dicData[key][1], dicData[key][2], dicData[key][3]))
   