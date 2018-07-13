import socket  # Import socket module
import pyaes
import rsa

(server_public, server_private) = rsa.newkeys(128)

port = 60000  # Reserve a port for your service.
s = socket.socket()  # Create a socket object
host = socket.gethostname()  # Get local machine name
s.bind((host, port))  # Bind to the port
s.listen(5)  # Now wait for client connection.
iv = "InitializationVe"
print 'Server listening....'
key = str(server_public)


while True:
    conn, addr = s.accept()  # Establish connection with client.
    print 'Got connection from', addr
    hello = conn.recv(1024)
    print('Server received', repr(hello))
    if hello == "Ahoy!":
        dic = {'key': key}
        conn.send(dic['key'])
        aes_key1 = conn.recv(16)
        client_aes_key1 = rsa.decrypt(aes_key1,server_private)

        aes_key2 = conn.recv(16)
        client_aes_key2 = rsa.decrypt(aes_key2, server_private)

        aes_key3 = conn.recv(16)
        client_aes_key3 = rsa.decrypt(aes_key3, server_private)

        aes_key4 = conn.recv(16)
        client_aes_key4 = rsa.decrypt(aes_key4, server_private)
        client_aes_key = client_aes_key1 + client_aes_key2+client_aes_key3+client_aes_key4

        print(client_aes_key)
        print("client aes key received")

        aes = pyaes.AESModeOfOperationCBC(client_aes_key, iv=iv)

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



