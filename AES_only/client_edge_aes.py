import socket                   # Import socket module
import time
import pyaes
import csv
import os

csvfile = open("AES_only/results2.csv",'wb')
writer = csv.writer(csvfile)
folder = "features/6_10_people"
all_files = os.listdir(folder)

for each in all_files:
    filename = folder + "/" + each

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
    # filename = '13.0.1.txt'

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
            # print(l)
            spaces = 16 - len(l)
            str_len = len(l) + spaces
            l = l.ljust(str_len)

    f.close()

    print("Sending the file completed")
    time_end = time.time()

    duration_time = time_end - time_start

    print("Time taken is ", str(duration_time))
    variables = []
    variables.append(each)
    variables.append(str(duration_time))
    writer.writerow(variables)

csvfile.close()

