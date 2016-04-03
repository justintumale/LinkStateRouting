import threading
import forward_echo_thread

class ForwardEchoListener(threading.Thread):
    forward_echo_socket = ''


    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.forward_echo_socket = socket

    def run(self):
        forward_echo_data, forward_echo_address = self.forward_echo_socket.recvfrom(1024)
        forward_echo_THREAD = forward_echo_thread.ForwardEchoThread(forward_echo_data, forward_echo_address, self.forward_echo_socket)
        forward_echo_THREAD.start()
        forward_echo_THREAD.join()



