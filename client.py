"""
A Simple Client class that allows to configure a socket client in a very simple
way. It is for test purposes only.
"""

import socket


__author__ = "Facundo Victor"
__license__ = "MIT"
__email__ = "facundovt@gmail.com"


class SimpleClient(object):
    """Simple client using the socket library"""

    def __init__(self, connection_oriented=True):
        """
        The constructor initializes a socket client specifying the if it must
        be a connection oriented socket.

        :param connection_oriented: A flag that specifies if the socket must
                                    be connection oriented or not
        :ptype: Boolean
        """
        self.connection_oriented = connection_oriented
        if connection_oriented:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def connect(self, host, port):
        """
        Connects the socket to the "host:port"

        :param host: The network layer identifier of the server.
        :ptype: String or Integer (see help(socket))

        :param port: The transport layer identifier of a server application.
        :ptype: Integer
        """
        server_address = (host, port)
        self.server = server_address
        if self.connection_oriented:
            self.sock.connect(server_address)
            print('Socket connected to %s port %s' % server_address)
        else:
            print('Socket ready to interact to %s port %s' % server_address)

    def close_connection(self, sock=None):
        """
        Properly close a socket doing a shudown first.

        :param sock: The sockt to close, The default is the self.sock socket.
        :ptype: socket
        """
        if sock is None:
            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.close()
        else:
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()

    def send(self, message):
        """
        Sends the message to the server.

        :param message: The message to be transmitted to the server.
        :ptype: String

        :raises RuntimeError: socket connection broken.
        """
        if self.connection_oriented:
            total_sent = 0
            while total_sent < len(message):
                sent = self.sock.send(message[total_sent:])
                if sent is 0:
                    raise RuntimeError("socket connction broken")
                total_sent += sent
        else:
            self.sock.sendto(message, self.server)

    def receive(self, amount):
        """
        Receives an amount of information from the server and returns it to be
        treated for the handler.

        :param amount: Amount of information to be recovered from the server
        :ptype: Integer

        :returns: The message received from the server.
        :rtype: String

        :raises RuntimeError: socket connection broken.
        """
        if self.connection_oriented:
            chunks = []
            bytes_recorded = 0
            while bytes_recorded < amount:
                chunk = self.sock.recv(min(amount - bytes_recorded, 2048))
                if chunk is '':
                    raise RuntimeError('socket connection broken')
                chunks.append(chunk)
                bytes_recorded += len(chunk)
            return ''.join(chunks)
        else:
            (message, server_address) = self.sock.recvfrom(amount)
            return message
