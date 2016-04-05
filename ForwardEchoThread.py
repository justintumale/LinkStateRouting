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
        raw_data = data.decode('utf-8')
        self.data = json.loads(raw_data)
        self.receiveAddress = address
        self.socket = socket

    def run(self):
        print('Running forward/echo thread...')
        print('parsing message...')
        from_node, to_node, message = self.parse_data(self.data)
        validation = self.validate(to_node)

        if validation is False:                 #if the node is not valid
            print("This node does not exist")
            return
        else:
            path = self.compute_shortest_path(from_node, to_node)

        if path == 0:
            # if the node is addressed to you, send it back to your client
            print('From', from_node, 'to', to_node, ':', message)
        else:
            print('this message was not addressed to you')
            pass


    def parse_data(self, data):
        """
        Convert the json message to a dictionary
        :return: the dictionary
        """
        #print(data)
        #data = json.loads(data)
        from_node = data['from_node']
        to_node = data['to_node']
        msg = data['msg']

        return ''.join(from_node.strip()), ''.join(to_node.strip()), ''.join(msg)

    def validate(self, to_node):
        #TODO check if node exists
        #TODO check if there is a path to the node
        if 1 == 2:
            return False
        else:
            return True


    def compute_shortest_path(self, from_node, to_node):
        self.OVERLAY_NETWORK = self.OVERLAY_NETWORK
        if to_node == 'fjt14188':
            return 0
        else:
            return True

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