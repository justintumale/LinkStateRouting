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
        '''
        Parse the data and forward the message to it's proper destination.
        :return:
        '''

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
        '''
        Forward the message to its proper destination.
        :param from_node:   the root node
        :param to_node:     the destination node
        :param msg:         the message
        :return:
        '''

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


                #FORWARD FROM ROUTER TO CLIENT
                forward_message = echomessage.EchoMessage(from_node, to_node, msg)
                forward_message = json.dumps(forward_message.__dict__)

                self.socket.sendto(forward_message.encode('utf-8'), ('127.0.0.1', 5002))
                #print('receive Address', self.receiveAddress)


                if msg.startswith("Received:"):
                    return
                #REPLY TO SENDER IF THE MESSAGE DOES NOT START WITH "Received:"
                path = self.compute_shortest_path('fjt14188', from_node, self.OVERLAY_GRAPH)
                destination = path[1]
                destination_ports = self.NODE_PORT_MAP[destination]
                destination_address = destination_ports[1]
                ack_msg = 'Received: ' + msg
                ack_message = echomessage.EchoMessage('fjt14188', from_node, ack_msg)
                ack_message = json.dumps(ack_message.__dict__)
                self.socket.sendto(ack_message, ('127.0.0.1', destination_address))



                self.socket.sendto(forward_message.encode('utf-8'), ("127.0.0.1", destination_address))

                return

            else:
                #compute shortest path

                path = self.compute_shortest_path(from_node, to_node, self.OVERLAY_GRAPH)
                if path == None:

                    error_message = "Error: No existing path to " + to_node + "."
                    print(error_message)

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

                    #ack to my client
                    '''
                    reply_message = 'forwarding message to ' + destination
                    print(reply_message)
                    ack = echomessage.EchoMessage(from_node, to_node, reply_message)
                    ack = json.dumps(ack.__dict__)
                    self.socket.sendto(ack.encode('utf-8'), self.receiveAddress)
                    '''


                    forward_message = echomessage.EchoMessage(from_node, to_node, msg)
                    forward_message = json.dumps(forward_message.__dict__)

                    self.socket.sendto(forward_message.encode('utf-8'), ("127.0.0.1", destination_address))

                    return

    def validate(self, to_node):
        '''
        Validate if the node exists in the map of all nodes.
        :param to_node:
        :return:
        '''
        if to_node not in self.OVERLAY_GRAPH:
            return False
        else:
            return True

    def compute_shortest_path(self, from_node, to_node, OVERLAY_GRAPH):
        '''
        Call dijkstra's algorthm and return the shortest path.
        :param from_node:    the root node
        :param to_node:     the destination node
        :param OVERLAY_GRAPH:   the overlay graph
        :return:        the shortest path
        '''

        path = Dijkstra.dijkstras(from_node, to_node, OVERLAY_GRAPH)
        return path

