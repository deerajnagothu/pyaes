import socket                   # Import socket module
import time
import rsa



time_start = time.time()
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

(client_rsa_pub,client_rsa_priv) = rsa.newkeys(128)

print(client_rsa_pub)


s.connect((host, port))
s.send("Ahoy!")

print 'receiving key'
key = s.recv(128)
print(key)

r = key.split('(')
key_main = r[1].split(",")


e = key_main[1].split(')')
n = key_main[0]

server_pub_key = rsa.PublicKey(n= long(n),e= int(e[0]))
print(type(server_pub_key))

# server_pub_rsa = client_rsa_pub
# server_pub_rsa['n'] = n
# server_pub_rsa['e'] = e

filename = 'google-10000-english.txt'
f = open(filename, 'rb')
l = f.read(5)
while (l):
    msg = l.encode('utf8')
    crypt_msg = rsa.encrypt(msg,server_pub_key)
    s.send(crypt_msg)
    #print('Sent ', repr(l))
    l = f.read(5)

f.close()

print("Sending the file completed")
time_end = time.time()

duration_time = time_end - time_start

print("Time taken is ", str(duration_time))

