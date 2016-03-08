"""
A Simple example for testing the SimpleServer Class. A simple telnet server.
It is for studying purposes only.

To try it, just execute "telnet localhost 7878"
"""

from simple.server import SimpleServer


__author__ = "Facundo Victor"
__license__ = "MIT"
__email__ = "facundovt@gmail.com"


def handle_message(sockets=None):
    """
    Handle a simple TCP connection.
    """
    if sockets is not None:
        (readable, writable, errors) = sockets
        try:
            while True:
                data = readable.recv(1024)
                print('Received data: %s' % (data))
                if data:
                    print('Sending a custom ACK to the client')
                    writable.sendall("Received ;)\n")
                else:
                    print('Received empty data')
                    break
        finally:
            SS.close_connection()


SS = SimpleServer(blocking=True)
SS.register_handler(handle_message)
SS.bind_and_listeen("localhost", 7878)
