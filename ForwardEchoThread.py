import threading
import json
import echomessage


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
        print('parsing message...')
        parsed_message = self.parse_echo_message(self.data)
        print(parsed_message)

    def parse_echo_message(self, data):
        """
        after an echo_message is received, determine if it should be forwarded to another
        router or sent back to our client
        :return:
        """
        msg = echomessage.EchoMessage('a', 'b', 'message')
        jsonText = json.dumps(msg.__dict__)
        #print ('Json Encoding: '+jsonText)
        return jsonText


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