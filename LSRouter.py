import socket
import forward_echo_thread
import threading

class LSRouter:
    host = ''
    LM_receive_port = ''
    LM_receive_socket = ''
    forward_echo_port = ''
    forward_echo_socket = ''
    OVERLAY_GRAPH = ''


    def __init__(self):
        self.host = "127.0.0.1"

        self.LM_receive_port = 50020
        self.LM_receive_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.LM_receive_socket.bind((self.host, self.LM_receive_port))

        self.forward_echo_port = 50021
        self.forward_echo_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.forward_echo_socket.bind((self.host, self.forward_echo_port))

    def initialize_link_table(self):
        """
        Initialize the link table.
        :return:
        """
        pass


    def run(self):
        print('Running router...')
        while True:
            #LMdata, LMaddress = self.LM_receive_socket.recv(1024)
            forward_echo_data, forward_echo_address = self.forward_echo_socket.recvfrom(1024)
            forward_echo_THREAD = forward_echo_thread.ForwardEchoThread(forward_echo_data, forward_echo_address, self.forward_echo_socket)
            forward_echo_THREAD.start()
            forward_echo_THREAD.join()


def Main():
    a = LSRouter()
    a.run()


if __name__ == '__main__':
    Main()