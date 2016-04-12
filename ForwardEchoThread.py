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

            error_message = "Error: This node does not exist"
            forward_message = echomessage.EchoMessage(from_node, to_node, error_message)
            forward_message = json.dumps(forward_message.__dict__)

            destination_node = self.NODE_PORT_MAP[from_node]
            destination_port = destination_node[1]

            self.socket.sendto(forward_message.encode('utf-8'), ("127.0.0.1", destination_port))

            return
        else:

            if to_node == 'fjt14188':
                # if the node is addressed to you, send it back to your client

                forward_message = echomessage.EchoMessage(from_node, to_node, msg)
                forward_message = json.dumps(forward_message.__dict__)

                self.socket.sendto(forward_message.encode('utf-8'), ('127.0.0.1', 5002))
                print('receive Address', self.receiveAddress)

                return

            else:
                #compute shortest path

                path = self.compute_shortest_path(from_node, to_node, self.OVERLAY_GRAPH)
                if path == None:
                    error_message = "Error: No existing path to " + to_node + "."

                    forward_message = echomessage.EchoMessage('fjt14188', from_node, error_message)
                    forward_message = json.dumps(forward_message.__dict__)


                    destination_node = self.NODE_PORT_MAP[from_node]
                    destination_port = destination_node[1]
                    self.socket.sendto(forward_message.encode('utf-8'), ("127.0.0.1", destination_port))

                    return

                else:
                    #select the node to send it to
                    destination = path[1]
                    destination_ports = self.NODE_PORT_MAP[destination]
                    destination_address = destination_ports[1]


                    reply_message = 'forwarding message to ' + destination
                    ack = echomessage.EchoMessage(from_node, to_node, reply_message)
                    ack = json.dumps(ack.__dict__)
                    self.socket.sendto(ack.encode('utf-8'), self.receiveAddress)


                    forward_message = echomessage.EchoMessage(from_node, to_node, msg)
                    forward_message = json.dumps(forward_message.__dict__)

                    self.socket.sendto(forward_message.encode('utf-8'), ("127.0.0.1", destination_address))

                    return

    def validate(self, to_node):
        if to_node not in self.OVERLAY_GRAPH:
            return False
        else:
            return True

    def compute_shortest_path(self, from_node, to_node, OVERLAY_GRAPH):

        path = Dijkstra.dijkstras(from_node, to_node, OVERLAY_GRAPH)
        return path

