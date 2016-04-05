import threading

class LinkMessageBroadcast(threading.Thread):

    LINKS = []
    LM_socket = ''
    NODE_PORT_MAP = ''

    def __init__(self, LM_socket, LINKS, NODE_PORT_MAP):
        threading.Thread.__init__(self)
        self.LINKS = LINKS
        self.LM_socket = LM_socket
        self.NODE_PORT_MAP = NODE_PORT_MAP

    def run(self):
        print('Running Broadcaster...')

        for i in self.LINKS:
            pass
