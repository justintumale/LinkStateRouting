import threading
import socket
import linkmsg
import json


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
        for link in self.LINKS:
            my_link = linkmsg.LinkMsg('fjt14188', link)
            my_link_json = json.dumps(my_link.__dict__)

            for key, value in self.NODE_PORT_MAP.items():
                port = value[0]
                #print('sending to this port: ', port)
                server = (self.host, port)
                self.LM_receive_socket.settimeout(.001)
                self.LM_receive_socket.sendto(my_link_json.encode('utf-8'), server)



    #host = '127.0.0.1'
    #'''port has to be different from udpServer's.'''
    #port = 5001

    #'''the server is on this machine, but its port is on the udpServer??'''
    #server = (host, 5000)
    #'''create the udp socket'''
    #s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #'''bind the socket to the port'''
    #s.bind((host, port))

    '''
    myport = 24709
    server = (host, index)          #24708

    s.settimeout(1)

    s.sendto(message.encode('utf-8'), server)
    data, address = s.recvfrom(index)
    data = data.decode('utf-8')
    '''
