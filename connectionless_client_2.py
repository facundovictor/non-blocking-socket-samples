"""
A simple connectionless client. It is for studying purposes only.
"""

import socket


__author__ = "Facundo Victor"
__license__ = "MIT"
__email__ = "facundovt@gmail.com"


def do_some_messaging(host, port):
    """
    Handle a simple UDP client. Ask for stdinput data and send it to the UDP
    server.

    :param host: Name or IP address of the destination server.
    :ptype: String or Integer (see help(socket))

    :param port: The transport layer identifier of an application
    :ptype: Integer
    """
    server = (host, port)
    while True:
        data = raw_input('Please enter data to send:\n')
        if data.strip() == 'exit':
            return

        print('Sending a data to the server')
        sock.sendto(data, server)
        (new_data, server_address) = sock.recvfrom(1024)
        print('Received data: %s' % (new_data))


"""
Take in mind that the connect only stores the host and the port, it does not
establishes any connection.
"""
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
do_some_messaging("localhost", 8888)
sock.close()
