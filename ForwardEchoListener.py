import threading
import ForwardEchoThread

class ForwardEchoListener(threading.Thread):
    forward_echo_socket = ''


    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.forward_echo_socket = socket

    def run(self):
        print('Running Forward Echo Listener...')
        while True:
            forward_echo_data, forward_echo_address = self.forward_echo_socket.recvfrom(1024)
            forward_echo_THREAD = ForwardEchoThread.ForwardEchoThread\
                (forward_echo_data, forward_echo_address, self.forward_echo_socket)
            forward_echo_THREAD.start()
            forward_echo_THREAD.join()



