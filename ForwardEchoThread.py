import threading


class ForwardEchoThread(threading.Thread):

    data = ''
    receiveAddress = ''
    socket = ''

    OVERLAY_NETWORK = ''

    def __init__(self, data, address, socket):
        threading.Thread.__init__(self)
        self.data = data.decode('utf-8')
        self.receiveAddress = address
        self.socket = socket

    def run(self):
        print('Running forward/echo thread...')
        print('Message to forward:', self.data)

    def parse_echo_message(self):
        """
        after an echo_message is received, determine if it should be forwarded to another
        router or sent back to our client
        :return:
        """
        pass

    def compute_shortest_path(self, OVERLAY_NETWORK):
        self.OVERLAY_NETWORK = OVERLAY_NETWORK
        pass

    def echo_reply(self):
        '''If the message received is addressed to our Client, send it to the Client.
           If the Client is attempting to route to an invalid destination, also send
           an echo reply back to the Client.
        '''
        error = False

        if error is True:
            pass
        else:
            pass
        pass

    def forward(self):
        pass