import threading
import json
import echomessage
import Dijkstra
import OverlayGraph


class ForwardEchoThread(threading.Thread):

    data = ''
    receiveAddress = ''
    socket = ''
    LINKS = []
    OVERLAY_GRAPH = OverlayGraph.OVERLAY_GRAPH
    NODE_PORT_MAP = {}

    def __init__(self, data, address, socket, LINKS, NODE_PORT_MAP):
        threading.Thread.__init__(self)
        raw_data = data.decode('utf-8')
        self.data = json.loads(raw_data)
        self.receiveAddress = address
        self.socket = socket
        self.LINKS = LINKS
        self.NODE_PORT_MAP = NODE_PORT_MAP

    def run(self):
        print('Running forward/echo thread...')
        print('parsing message...')

        from_node, to_node, message = self.parse_data(self.data)

        self.forward(from_node, to_node, message)

    def parse_data(self, data):
        """
        Convert the json message to a dictionary
        :return: the dictionary
        """
        from_node = data['from_node']
        to_node = data['to_node']
        msg = data['msg']

        return ''.join(from_node.strip()), ''.join(to_node.strip()), ''.join(msg)

    def forward(self, from_node, to_node, msg):

        validation = self.validate(to_node)

        if validation is False:                 #if the node is not valid
            #TODO send back to client
            error_message = "Error: This node does not exist"
            self.socket.sendto(error_message)
            return
        else:

            if to_node == 'fjt14188':
                # if the node is addressed to you, send it back to your client
                print('From', from_node, 'to', to_node, ':', msg)
                forward_message_proxy = 'From', from_node, 'to', to_node, ':', msg
                forward_message = str(forward_message_proxy)
                self.socket.sendto(forward_message.encode('utf-8'), self.receiveAddress)
            else:
                #TODO forward to other client
                path = self.compute_shortest_path(from_node, to_node, self.OVERLAY_GRAPH)
                destination = path[1]
                destination_address = self.NODE_PORT_MAP[destination]

                #print('this message was not addressed to you')
                reply_message = 'forwarding message to ' + destination
                self.socket.sendto(reply_message.encode('utf-8'), self.receiveAddress)

                forward_message_proxy = 'From', from_node, 'to', to_node, ':', msg
                forward_message = str(forward_message_proxy)
                self.socket.sendto(forward_message.encode('utf-8'), destination_address)


    def validate(self, to_node):
        #TODO check if node exists
        #TODO check if there is a path to the node
        if 1 == 2:
            return False
        else:
            return True

    def compute_shortest_path(self, from_node, to_node, OVERLAY_GRAPH):

        path = Dijkstra.dijkstras(from_node, to_node, OVERLAY_GRAPH)
        return path
