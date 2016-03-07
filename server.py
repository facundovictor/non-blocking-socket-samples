"""
A Simple Server class that allows to configure a socket in a very simple way.
It is for studying purposes only.
"""

import socket
import sys


__author__ = "Facundo Victor"
__license__ = "MIT"
__email__ = "facundovt@gmail.com"


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
        self.blocking = blocking
        if not blocking:
            self.sock.setblocking(0)
            # Sockets from which we expect to read
            self.inputs = [self.sock]
            # Sockets to which we expect to write
            self.outputs = []
        # Socket registered handlers
        self.handlers = []

    def bind_and_listeen(self, host, port, max_conn=5):
        """
        Binds the socket to the "host", and prepares it to listen on "port"
        respecting a maximum of "max_connections"

        :param host: The network layer identifier of an interface
        :ptype: String or Integer (see help(socket))

        :param port: The transport layer identifier of an application
        :ptype: Integer

        :param max_conn: Number of unaccepted connections that the system will
                         allow before refusing new connections.
        :ptype: Integer
        """
        server_address = (host, port)
        self.sock.bind(server_address)
        self.sock.listen(max_conn)
        print('Socket binded to %s port %s,' % server_address + (max_conn,))
        if self.blocking:
            self.manage_simple_connection()
        else:
            self.manage_connections()

    def register_handler(self, handler):
        """
        Register a handler method to be executed on accepted connections. It
        must have the tuple (input: Socket, output: Socket, error: Socket) as
        an argument. If the handler already is registered, the method returns
        False.

        :param handler: Socket event handler
        :ptype: Method

        :returns: True if the handler is registered, False in other case.
        :rtype: Boolean
        """
        if self.is_registered(handler):
            return False
        else:
            self.handlers += [handler]
            return True

    def unregister_handler(self, handler):
        """
        Unregister the handler so it no longer will be executed on accepted
        connections.

        :param handler: Socket event handler
        :ptype: Method

        :returns: True if the handler is unregistered, False in other case.
        :rtype: Boolean
        """
        try:
            self.handlers.remove(handler)
            return True
        except ValueError:
            return False

    def is_registered(self, handler):
        """
        Verify if the handler is registered.

        :param handler: Socket event handler
        :ptype: Method

        :returns: True if the handler is registered, False in other case.
        :rtype: Boolean
        """
        try:
            self.handlers.index(handler)
            return True
        except ValueError:
            return False
