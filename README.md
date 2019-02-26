# Assignment 1: Getting familiar with Sockets

## Author

```text
Name: Ilan Kleiman
ID: 110942711
```

## Requirements

- Python3

## Usage

1. Edit `server.py` to run on the port you want. If you're running this script on a server, you may want to change the address from `localhost` to the IPV4/6 address of the server.

2. Run `server.py`
    - e.g: `$ python3 server.py`

3. Edit `client.py` to request the email address you want to specify...
    - i.e: At the bottom of `client.py`, by default there's `abClient.setMessageData('bill@microsoft.com')` ... You can change the email...

4. Run `client.py`
    - e.g: `$ python3 client.py`

## Description

The server checks for any connections, once a connection is made; it reads the first 2 bytes...

The second byte specifies how long the rest of the message is (as per assignment instructions).

The server then reads for the next X# of bytes that was previously specified from the prior byte... The result is an email address which is then looked up in a 'database'. For this assignment, a simple dictionary (data structure) is used as a mock database.

The server then responds to the client with the first byte specifying it's a response packet (R). The byte specifies the rest of the response size... The client then reads for previously specified amount of bytes (the prior byte specifies size). The read result is the full name of the supplied email address.