# Script Python pour effectuer un ping
#Jean-Bernard Altidor
#---------------------------------------
import socket
import time

ttl = 50 
socket.setdefaulttimeout(0.5) 

def ping(port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
   s.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
   con = s.connect_ex((IP, port))
   if (con == 0):
         delta = time.time() - startTime
         print('Ping to {}:{} succeded. TTL = {} time={:.3f} ms'.format(IP,port,ttl,delta*1000))
   else:
          print('{}:{} is closed'.forma(IP,port)) 
  


IP = raw_input('Enter the IP : ')
port = input('Enter the port : ') 
startTime = time.time() 
ping (port) 
