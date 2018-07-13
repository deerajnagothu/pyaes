import socket                   # Import socket module
import pyaes

port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.
iv = "InitializationVe"
print 'Server listening....'
key = "1234567891234567"
aes = pyaes.AESModeOfOperationCBC(key, iv = iv)
while True:
    conn, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    hello = conn.recv(1024)
    print('Server received', repr(hello))
    if hello == "Ahoy!":
        dic = {'key':"1234567891234567"}
        conn.send(dic['key'])

        with open('server_13.0.1.txt', 'wb') as f:
            print "Server is ready to receive !"

            while True:
                data = conn.recv(16)
                print(data)


                # print('data=', data)
                if not data:
                    break
                txt = aes.decrypt(data)
                f.write(txt)

    f.close()


    print("Successfully got the file !")
    conn.close()
    print("Connection Closed !")

    print("Now waiting for new connection again !")



