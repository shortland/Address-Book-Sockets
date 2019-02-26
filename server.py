import socket
import sys

class AddressBookServer(object):
    # a temporary mockup database lookup...
    def getNameFromFakeDB(self, fakeEmail):
        someDatabase = {
            'ilan.kleiman@stonybrook.edu': 'Ilan Kleiman',
            'abc@stonybrook.edu': 'abcdef abd',
            'bill@microsoft.com': 'Bill Gates'
        }
        return someDatabase.get(fakeEmail, 'USER NOT FOUND')

    # setup the server on the specified host and port
    def serverSetup(self, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Connection open on %s port %s' % (host, port))
        sock.bind((host, port))
        sock.listen(1)

        # constantly check for new connections to accept
        while True:
            print('Waiting for new connections...')
            connection, client_address = sock.accept()

            # when a connection is made attempt to parse it out below
            try:
                print('Connection from', client_address)

                # first byte specifies message type
                messageType = chr(ord(connection.recv(1)))
                print("Message Type: %s" % messageType)

                # second byte specifies message length
                messageLength = ord(connection.recv(1))
                print("Message Length: %d" % messageLength)

                # third byte specifies message text, AKA the email address to read
                # reads a specified amount of bytes that was previously described above
                messageText = (connection.recv(messageLength)).decode("utf-8")
                print("Message Text: %s" % messageText)

                # database lookup
                nameFromDB = self.getNameFromFakeDB(messageText)
                print("Name from DB: %s" % nameFromDB)
                
                # prepare the data to send back to the client & send it
                responseLength = chr(len(nameFromDB))
                dataToSend = ("R%s%s" % (responseLength, nameFromDB))
                connection.sendall(str.encode(dataToSend))
                print(dataToSend)
            
            # close the socket since we're done parsing the client request
            finally:
                print("Socket Closed.")
                connection.close()

# create AddressBookServer object
abServer = AddressBookServer()
# begin looking for new connections on the specified host and address
abServer.serverSetup('localhost', 4311)