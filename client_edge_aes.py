import socket                   # Import socket module
import time
import pyaes

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.


time_start = time.time()
s.connect((host, port))
s.send("Ahoy!")

print 'receiving key'
key = s.recv(16)
print(key)
iv = "InitializationVe"
filename = 'google-10000-english.txt'

encrypter = pyaes.Encrypter(pyaes.AESModeOfOperationCBC(key, iv))
ciphertext = ''
for line in file(filename):

    ciphertext += encrypter.feed(line)

ciphertext += encrypter.feed()

c = open('ciphertext.txt', 'w')
c.write(ciphertext)
c.close()

f = open('ciphertext.txt','rb')
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

