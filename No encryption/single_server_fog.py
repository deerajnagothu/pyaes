import socket                   # Import socket module

port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print 'Server listening....'

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    hello = conn.recv(1024)
    print('Server received', repr(hello))
    if hello == "Ahoy!":
        dic = {'key':"1234567891234567"}
        conn.send(dic['key'])

        with open('Receive/server_receive_text.txt', 'wb') as f:
            print "Server is ready to receive !"

            while True:
                data = conn.recv(16)
                # print('data=', data)
                if not data:
                    break
                f.write(data)

    f.close()

    print("Successfully got the file !")
    conn.close()
    print("Connection Closed !")

    print("Now waiting for new connection again !")


