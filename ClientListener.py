import threading
import socket

class ClientListener(threading.Thread):
    socket = ''

    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.socket = socket

    def run(self):
        while True:
            data, address = self.socket.recvfrom(1024)
            data = data.decode('utf-8')
            print('Router response:', data)