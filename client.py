import socket
import sys

class AddressBookClient(object):
    def __init__(self):
        self.sock = None
        self.messageType = 'Q'
        self.messageLength = None
        self.messageText = None
    
    # set the text of the message to send...
    # raises an error if it's too large
    def setMessageData(self, messageText):
        if len(messageText) >= 255:
            raise Exception('Message too long!')
        else:
            self.messageLength = len(messageText)
            self.messageText = messageText

    # method to send set message to the specified port and host
    def sendMessage(self, host, port):
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # creates a connection ...
        print('Created connection to %s:%s' % (host, port))
        connection.connect((host, port))

        try:
            # Maintains 1b size for the packet-length field
            dataToSend = ("%s%s%s" % (self.messageType, chr(self.messageLength), self.messageText))
            
            # sends the above string in a packet... first byte-encodes it
            print('Sending Packet...')
            connection.sendall(str.encode(dataToSend))

            print('Waiting for server response...')

            # attempts to read the first two bytes one at a time, then reads the last bytes for the specified size...
            try:
                messageType = chr(ord(connection.recv(1)))
                print("Message Type: %s" % messageType)

                messageLength = ord(connection.recv(1))
                print("Message Length: %d" % messageLength)

                messageText = (connection.recv(messageLength)).decode("utf-8")
                print("Message Text: %s" % messageText)
            except:
                print("ERROR: Did not receieve proper response sizes...")
        
        # socket finished reading in input, we can close the client connection
        finally:
            print('Socket Closed.')
            connection.close()

# create the client object
abClient = AddressBookClient()
# set the email address we want to request the name for from the server
abClient.setMessageData('bill@microsoft.com')
# open and send the packet to the specified host and port
abClient.sendMessage('localhost', 4311)