"""
A Simple example for testing the SimpleServer Class. A simple connectionless
client. It is for studying purposes only.
"""

from client import SimpleClient


__author__ = "Facundo Victor"
__license__ = "MIT"
__email__ = "facundovt@gmail.com"


def do_some_messaging():
    """
    Handle a simple UDP client. Ask for stdinput data and send it to the UDP
    server.
    """
    while True:
        data = raw_input('Please enter data to send:\n')
        print('Sending a data to the server')
        SS.send(data)
        new_data = SS.receive(1024)
        print('Received data: %s' % (new_data))


SS = SimpleClient(connection_oriented=False)
"""
Take in mind that the connect only stores the host and the port, it does not
establishes any connection.
"""
SS.connect("localhost", 8888)
do_some_messaging()
SS.close_connection()
