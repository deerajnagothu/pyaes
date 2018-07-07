import socket                   # Import socket module
import time

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.


time_start = time.time()
s.connect((host, port))
s.send("Ahoy!")

print 'receiving key'
key = s.recv(16)
print(key)

filename = 'google-10000-english.txt'
f = open(filename, 'rb')
l = f.read(16)
while (l):
    s.send(l)
    # print('Sent ', repr(l))
    l = f.read(16)

f.close()

print("Sending the file completed")
time_end = time.time()

duration_time = time_end - time_start

print("Time taken is ", str(duration_time))

