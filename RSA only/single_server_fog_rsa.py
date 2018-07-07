import socket                   # Import socket module
import rsa
(server_public, server_private) = rsa.newkeys(128)
print(type(server_public['n']))
str_pub = str(server_public)
port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.


print 'Server listening....'
flag = 0
while True:
    conn, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    hello = conn.recv(1024)
    print('Server received', repr(hello))
    if hello == "Ahoy!":
        dic = {'key':str_pub}
        conn.send(dic['key'])

        with open('server_receive_text.txt', 'wb') as f:
            print "Server is ready to receive !"

            while True:
                data = conn.recv(16)
                # print('data=', data)
                if not data:
                    if flag == 0:
                        print("File receiving failed")
                    else:
                        print("Successfully got the file !")
                    break
                msg = rsa.decrypt(data,server_private)
                f.write(msg.decode('utf8'))
                flag = 1

    f.close()


    conn.close()
    print("Connection Closed !")

    print("Now waiting for new connection again !")


