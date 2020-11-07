
import socket
port = 33434 
max_hops = 40

def Traceroute(dest_name):  
    dest_addr = socket.gethostbyname(dest_name)
    icmp = socket.getprotobyname('icmp')
    udp = socket.getprotobyname('udp')
    ttl = 1
    while True:
        receiving_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp) #To send udp packets
        sending_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp) #To receive icmp packets

        sending_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl) #To set the TTL
        receiving_socket.bind(("", port)) #To specify the receving socket to listen on the given port
        sending_socket.sendto("testing", (dest_name, port)) #To specify the sending socket where and what to send
        
        current_hop = None
        curr_name = None

        try:
            data, current_hop = receiving_socket.recvfrom(512) #To receive the first 512 bits of the data send and the sender's address
            current_hop = current_hop[0]
            try:
                curr_name = socket.gethostbyaddr(current_hop)[0] #Translating the ip address to host name
            except socket.error:
                curr_name = current_hop
        except socket.error: #if icmp is disabled on the receiving end ,we may get an error ,so we use try/except
            print('timeout error')
        finally:
            sending_socket.close() #Closing the sockets
            receiving_socket.close()

        if current_hop is not None: #if the conversion was successfull add it to current address
            curr_host = "%s (%s)" % (curr_name, current_hop)
        else:
            curr_host = "*" # if not add "*"
        print "%d\t%s" % (ttl, curr_host)

        ttl += 1

        if current_hop == dest_addr or ttl > max_hops: #check if the destination has been reached or the max hop exceedd to exit
            break

if __name__ == "__main__":
    dest_name = raw_input('Enter the destination : ')
    print('Traceroute to {} ({}) on port : {}, {} hops max'.format(dest_name,socket.gethostbyname(dest_name),port,max_hops))
    startTime = time.time() 
    Traceroute(dest_name)