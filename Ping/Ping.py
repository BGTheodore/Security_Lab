# Script Python pour effectuer un ping
#Jean-Bernard Altidor
#---------------------------------------
import socket
import time

ttl = 50 
socket.setdefaulttimeout(0.5) 

def ping(IP,port):
  dest_addr = socket.gethostbyname(IP)
  icmp = socket.getprotobyname('icmp')
  udp = socket.getprotobyname('udp')
 

  receiving_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp) #To send udp packets
  sending_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp) #To receive icmp packets

  sending_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl) #To set the TTL
  receiving_socket.bind(("", port)) #To specify the receving socket to listen on the given port
  sending_socket.sendto("testing", (IP, port)) #To specify the sending socket where and what to send

  try:
            data, current_hop = receiving_socket.recvfrom(64) #To receive the first 512 bits of the data send and the sender's address
            current_hop = current_hop[0]
            curr_name = socket.gethostbyaddr(current_hop)[0] #Translating the ip address to host name
            
  except socket.error: #if icmp is disabled on the receiving end ,we may get an error ,so we use try/except
            pass
  finally:
            sending_socket.close() #Closing the sockets
            receiving_socket.close()

  if current_hop is not None: #if the conversion was successfull add it to current address
            #print ('Ping success!\t {}({})'.format(curr_name ,current_hop))
            delta = time.time() - startTime
            print('512 bits ping to {}:{} succeded! TTL = {} ms time={:.3f} ms'.format(dest_addr,port,ttl,delta*1000))
           
  else:
            print ('Ping failed!')

IP = raw_input('Enter the IP : ')
port = input('Enter the port : ') 
startTime = time.time() 
ping (IP,port) 
