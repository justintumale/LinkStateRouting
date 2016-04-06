import threading

class LinkMessageReceive(threading.Thread):
    data = ''
    address = ''
    LM_receive_socket = ''
    OVERLAY_GRAPH = {}

    def __init__(self, data, address, socket, OVERLAY_GRAPH):
        threading.Thread.__init__(self)
        self.data = data.decode('utf-8')
        self.address = address
        self.LM_receive_socket = socket
        self.OVERLAY_GRAPH = OVERLAY_GRAPH

    def run(self):
        print('Running Link Message Receiver...')
        #print('Link Message Receiver Overlay:', self.OVERLAY_GRAPH)
        print("LINK STATE MESSAGE RECEIVED: ", self.data)