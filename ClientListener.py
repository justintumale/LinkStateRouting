import threading
import socket

class ClientListener(threading.Thread):
    '''
    This class is responsible for listening to any incoming messages fro the client, and then
    printing the response.
    '''
    socket = ''
    flag = True

    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.socket = socket

    def run(self):
        while self.flag:
            data, address = self.socket.recvfrom(1024)
            data = data.decode('utf-8')
            print('Router response:', data)