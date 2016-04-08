import threading
import json
import OverlayGraph

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
        if 'fromNode' in data:
            from_node = data['fromNode']
        elif 'from_node' in data:
            from_node = data['from_node']

        if 'toNode' in data:
            to_node = data['toNode']
        elif 'to_node' in data:
            to_node = data['to_node']

        expiration = data['expiration']

       #return ''.join(from_node.strip()), ''.join(to_node.strip()), ''.join(expiration)
        return from_node, to_node, expiration

    def update_graph(self, from_node, to_node, expiration):
        #self.OVERLAY_GRAPH[from_node].append(to_node)
        OverlayGraph.create_link(from_node, to_node, expiration)