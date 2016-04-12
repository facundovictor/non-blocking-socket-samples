"""
A simple connection client. It is for studying purposes only.
"""

import socket


__author__ = "Facundo Victor"
__license__ = "MIT"
__email__ = "facundovt@gmail.com"


def do_some_messaging():
    """
    Handle a simple TCP client. Ask for stdinput data and send it to the TCP
    server.
    """
    while True:
        data = raw_input('Please enter data to send:\n')
        if data.strip() == 'exit':
            return

        print('Sending a data to the server')
        sock.send(data)

        new_data = sock.recv(2048)
        print('Received data: %s' % (new_data))


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = ("186.5.224.23", 9898)
sock.connect(server)

do_some_messaging()

sock.shutdown(socket.SHUT_RDWR)
sock.close()
