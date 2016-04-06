import threading
import LinkMessageReceive
import socket

class LinkStateListener(threading.Thread):

    LM_receive_socket = ''
    OVERLAY_GRAPH = {}

    def __init__(self, socket, OVERLAY_GRAPH):
        threading.Thread.__init__(self)
        self.LM_receive_socket = socket
        self.OVERLAY_GRAPH = OVERLAY_GRAPH

    def run(self):
        print('Running Link State Listener..')
        while True:
            try:
                link_message_data, link_message_address = self.LM_receive_socket.recvfrom(1024)

                LMReceiverThread = LinkMessageReceive.LinkMessageReceive\
                    (link_message_data, link_message_address, self.LM_receive_socket, self.OVERLAY_GRAPH)
                LMReceiverThread.start()
                LMReceiverThread.join()

            except socket.error:
                pass
