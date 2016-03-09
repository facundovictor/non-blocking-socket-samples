"""
A Simple example for testing the SimpleServer Class. A Simple non-blocking
server. It is for studying purposes only.
"""

import Queue

from simple.server import SimpleServer


__author__ = "Facundo Victor"
__license__ = "MIT"
__email__ = "facundovt@gmail.com"


def handle_readables(readable):
    """
    Handle multiple readable sockets.

    :param readable: Set of readable sockets.
    :ptype: socket[]
    """
    for s in readable:
        if s is SS.sock:
            # A "readable" server socket is ready to accept a connection
            connection, client_address = s.accept()
            connection.setblocking(0)
            SS.inputs.append(connection)

            # Give the connection a queue for data we want to send
            message_queues[connection] = Queue.Queue()
        else:
            data = s.recv(1024)
            (host, port) = s.getpeername()
            if data:
                print("Received data from %s:%s = \n%s" % (host, port, data))
                message_queues[s].put(data)
                if s not in SS.outputs:
                    SS.outputs.append(s)
            else:
                print("NO DATA: Closing client %s:%s" % (host, port))
                if s not in SS.outputs:
                    SS.outputs.remove(s)
                SS.inputs.remove(s)
                SS.close_connection(s)
                # Remove message queue
                del message_queues[s]


def handle_writables(writable):
    """
    Handle multiple writable sockets.

    :param writable: Set of writable sockets.
    :ptype: socket[]
    """
    for s in writable:
        try:
            # Get the message from the Queue
            next_msg = message_queues[s].get_nowait()
        except:
            print("Queue error for %s:%s" % s.getpeername())
            SS.outputs.remove(s)
        else:
            (host, port) = s.getpeername()
            print("Sending to %s:%s = \n%s" % (host, port, next_msg))
            s.send(next_msg)


def handle_exceptionals(exceptional):
    """
    Handle multiple sockets' exceptions.

    :param exceptional: Set of sockets on error state.
    :ptype: socket[]
    """
    for s in exceptional:
        print("Handling exceptional condifion for %s:%s" % s.getpeername())
        SS.inputs.remove(s)
        if s in SS.outputs:
            SS.outputs.remove(s)
        SS.close_connection(s)
        del message_queues[s]


def handle_sockets(sockets):
    """
    Handle multiple TCP connections.

    :param sockets: readabl/writable/on_exception sockets.
    :ptype: (socket[], socket[], socket[])
    """
    (readable, writable, exceptional) = sockets
    handle_readables(readable)
    handle_writables(writable)
    handle_exceptionals(exceptional)


# Outgoing message queues (socket:Queue)
message_queues = {}
SS = SimpleServer()
SS.register_handler(handle_sockets)
SS.bind_and_listeen("localhost", 9898)
