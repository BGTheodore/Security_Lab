# Script Python pour effectuer un ping
#Jean-Bernard Altidor
#---------------------------------------
import socket
import time

ttl = 0.5
socket.setdefaulttimeout(ttl) 

def ping(port):   
      recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
      send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
      send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
      recv_socket.bind(("", port))
      send_socket.sendto("", (IP, port))




IP = raw_input('Enter the IP : ')
port = input('Enter the port : ') 
startTime = time.time() 
ping (port) 
