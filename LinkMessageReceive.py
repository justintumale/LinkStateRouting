import threading

class LinkMessageReceive(threading.Thread):
    data = ''
    address = ''
    LM_receive_socket = ''

    def __init__(self, data, address, socket):
        threading.Thread.__init__(self)
        self.data = data
        self.address = address
        self.LM_receive_socket = socket

    def run(self):
        print('Running Link Message Receiver')