import socket                   # Import socket module
import time
import csv
csvfile = open("results2.csv",'wb')

import os
writer = csv.writer(csvfile)
folder = "../features/6_10_people"
all_files = os.listdir(folder)

for each in all_files:
    filename = folder+"/"+each


    s = socket.socket()             # Create a socket object
    host = socket.gethostname()     # Get local machine name
    port = 60000                    # Reserve a port for your service.


    time_start = time.time()
    s.connect((host, port))
    s.send("Ahoy!")

    print 'receiving key'
    key = s.recv(16)
    print(key)




    files = os.path.getsize(filename)
    filesi = str(files).split("L")
    filesize = filesi[0]




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
    print("Size of file", filesize)
    variables = []
    variables.append(each)
    variables.append(filesize)
    variables.append(str(duration_time))
    writer.writerow(variables)

csvfile.close()