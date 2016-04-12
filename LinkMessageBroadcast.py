import threading
import socket
import linkmsg
import json
import time
import OverlayGraph

class LinkMessageBroadcast(threading.Thread):

    LM_receive_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    NODE_PORT_MAP = {'key':'value'}
    host = ''
    LINKS = []

    def __init__(self, host, LM_receive_socket, NODE_PORT_MAP, LINKS):
        threading.Thread.__init__(self)
        self.LM_receive_socket = LM_receive_socket
        self.NODE_PORT_MAP = NODE_PORT_MAP
        self.host = host
        self.LINKS = LINKS

    def run(self):
        print('Running Broadcaster...')
        while True:
            for link in self.LINKS:
                #broadcast a message to all nodes informing them that you are connected to this link
                my_link = linkmsg.LinkMsg('fjt14188', link)
                my_link_json = json.dumps(my_link.__dict__)

                for key, value in self.NODE_PORT_MAP.items():
                    port = value[0]
                    #print('sending to this port: ', port)
                    server = (self.host, port)
                    self.LM_receive_socket.settimeout(.001)
                    self.LM_receive_socket.sendto(my_link_json.encode('utf-8'), server)
            time.sleep(30)
            OverlayGraph.print_graph()
