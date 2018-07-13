import socket                   # Import socket module
import time
import pyaes
import rsa
import csv
import os

csvfile = open("AES_RSA/results2.csv",'wb')
writer = csv.writer(csvfile)
folder = "features/6_10_people"
all_files = os.listdir(folder)

for each in all_files:
    filename = folder+"/"+each

    time_start = time.time()
    s = socket.socket()             # Create a socket object
    host = socket.gethostname()     # Get local machine name
    port = 60000                    # Reserve a port for your service.

    aes_key1 = "12345"
    aes_key2 = "67891"
    aes_key3 = "23456"
    aes_key4 = "7"

    s.connect((host, port))
    s.send("Ahoy!")

    print 'receiving key'
    key = s.recv(128)
    print(key)
    iv = "InitializationVe"
    # filename = 'google-10000-english.txt'

    r = key.split('(')
    key_main = r[1].split(",")


    e = key_main[1].split(')')
    n = key_main[0]

    server_pub_key = rsa.PublicKey(n= long(n),e= int(e[0]))
    print(type(server_pub_key))

    enc_aes_key = rsa.encrypt(aes_key1,server_pub_key)
    s.send(enc_aes_key)

    enc_aes_key = rsa.encrypt(aes_key2,server_pub_key)
    s.send(enc_aes_key)

    enc_aes_key = rsa.encrypt(aes_key3,server_pub_key)
    s.send(enc_aes_key)

    enc_aes_key = rsa.encrypt(aes_key4,server_pub_key)
    s.send(enc_aes_key)

    key = aes_key1 + aes_key2 + aes_key3 + aes_key4

    encrypter = pyaes.Encrypter(pyaes.AESModeOfOperationCBC(key, iv))
    ciphertext = ''

    aes = pyaes.AESModeOfOperationCBC(key, iv = iv)

    f = open(filename,'rb')
    l = f.read(16)
    while (l):
        #print(len(l))
        k = aes.encrypt(l)
        s.send(k)
        # print('Sent ', repr(l))
        l = f.read(16)
        if len(l) != 16 and len(l) != 0:
            #print(l)
            spaces = 16 - len(l)
            str_len = len(l) + spaces
            l = l.ljust(str_len)
            #print(l)


    f.close()

    print("Sending the file completed")
    time_end = time.time()

    duration_time = time_end - time_start
    print(duration_time)
    variables = []
    variables.append(each)
    variables.append(str(duration_time))
    writer.writerow(variables)

csvfile.close()
