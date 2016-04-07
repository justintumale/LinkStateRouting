import threading
import json

class LinkMessageReceive(threading.Thread):
    data = ''
    address = ''
    LM_receive_socket = ''
    OVERLAY_GRAPH = {}

    def __init__(self, data, address, socket, OVERLAY_GRAPH):
        threading.Thread.__init__(self)
        raw_data = data.decode('utf-8')
        self.data = json.loads(raw_data)
        self.address = address
        self.LM_receive_socket = socket
        self.OVERLAY_GRAPH = OVERLAY_GRAPH

    def run(self):
        print('Running Link Message Receiver...')
        #print('Link Message Receiver Overlay:', self.OVERLAY_GRAPH)
        print("LINK STATE MESSAGE RECEIVED: ", self.data)
        from_node, to_node, expiration = self.parse_data(self.data)
        self.update_graph(from_node, to_node, expiration)

    def parse_data(self, data):
        """
        Convert the json message to a dictionary
        :return: the dictionary
        """
        from_node = data['fromNode']
        to_node = data['toNode']
        expiration = data['expiration']


        print('from node', from_node)
        print('to node', to_node)
        print('exipration', expiration)



       #return ''.join(from_node.strip()), ''.join(to_node.strip()), ''.join(expiration)
        return from_node, to_node, expiration

    def update_graph(self, from_node, to_node, expiration):
        self.OVERLAY_GRAPH[from_node].append(to_node)