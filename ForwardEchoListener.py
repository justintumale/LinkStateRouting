import threading
import ForwardEchoThread
import socket

class ForwardEchoListener(threading.Thread):
    '''
    A class that listens for incoming echo/forward messages.
    '''
    forward_echo_socket = ''
    LINKS = []
    NODE_PORT_MAP = {}

    def __init__(self, socket, LINKS, NODE_PORT_MAP):
        '''
        Initialize the socket, our node's current links, and the node port map.
        '''
        threading.Thread.__init__(self)
        self.forward_echo_socket = socket
        self.LINKS = LINKS
        self.NODE_PORT_MAP = NODE_PORT_MAP

    def run(self):
        '''
        Listen for incoming echo/forward messages.
        :return:
        '''
        print('Running Forward Echo Listener...')
        while True:
            try:
                forward_echo_data, forward_echo_address = self.forward_echo_socket.recvfrom(1024)
                forward_echo_THREAD = ForwardEchoThread.ForwardEchoThread\
                    (forward_echo_data, forward_echo_address, self.forward_echo_socket, self.LINKS, self.NODE_PORT_MAP)
                forward_echo_THREAD.start()
                forward_echo_THREAD.join()
            except socket.error:
                pass



