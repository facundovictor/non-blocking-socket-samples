import socket
import sys


class SimpleServer(object):
    """Simple server using the socket library"""

    def __init__(self, blocking=False, connection_oriented=True):
        """
        The constructor initializes socket specifying the blocking status and
        if it must be a connection oriented socket.

        :param blocking: A flag that specifies if the socket must be blocking
        :ptype: Boolean

        :param connection_oriented: A flag that specifies if the socket must
                                    be connection oriented or not
        :ptype: Boolean
        """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if not blocking:
            self.sock.setblocking(0)

    def connect(self, host, port):
        """
        Connects the server to the "host", and prepares it to listen on "port"

        :param host: The network layer identifier of an interface
        :ptype: String or Integer (see help(socket))

        :param port: The transport layer identifier of an application
        :ptype: Integer
        """
        self.sock.connect((host, port))
