import socket, sys               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
addr = '192.168.1.101'
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

if (sys.argv[1] == "connect"):
    host = sys.argv[2]
    s.connect((host, port))
    s.close 
else:
    s.listen(5)                 # Now wait for client connection.
    while True:
       c, addr = s.accept()     # Establish connection with client.
       c.send('Thank you for connecting')
       c.close()
