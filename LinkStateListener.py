import threading
import LinkMessageReceive

class LinkStateListener(threading.Thread):

    LM_receive_socket = ''

    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.LM_receive_socket = socket

    def run(self):
        print('Running Link State Listener..')
        while True:
            link_message_data, link_message_address = self.LM_receive_socket.recvfrom(1024)
            LMReceiverThread = LinkMessageReceive.LinkMessageReceive\
                (link_message_data, link_message_address, self.LM_receive_socket)
            LMReceiverThread.run()
            #LMReceiverThread.join()