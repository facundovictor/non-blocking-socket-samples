"""
A Simple example for testing the SimpleServer Class. A simple connectionless
server. It is for studying purposes only.
"""

from server import SimpleServer


__author__ = "Facundo Victor"
__license__ = "MIT"
__email__ = "facundovt@gmail.com"


def handle_message(sockets=None):
    """
    Handle a simple UDP client.
    """
    if sockets is not None:
        (readable, writable, errors) = sockets
        try:
            while True:
                (data, address) = readable.recvfrom(1024)
                print('Received data: %s from %s' % (data, address))
                if data:
                    print('Sending a custom ACK to the client %s \
                          '.format(address))
                    writable.sendto("Received ;)\n", address)
                else:
                    print('Received empty data')
                    break
        finally:
            SS.close_connection()


SS = SimpleServer(connection_oriented=False)
SS.register_handler(handle_message)
SS.bind_and_listeen("localhost", 8888)
