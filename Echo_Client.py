import socket

class EchoClient:
    host = ''
    port = ''
    socket = ''
    router = ''

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 5001
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.host, self.port))

        self.router = (self.host, 50021) #router port

    def send_echo(self):
        '''Sends an echo message to the LSRouter'''
        pass

    def receive_echo(self):
        '''Receives an echo message from the LSRouter'''
        pass

    def run(self):
        message = input('->')
        while message is not 'quit':
            self.socket.sendto(message.encode('utf-8'), self.router)
            message = input('->')


def Main():
    client = EchoClient()
    client.run()

if __name__ == '__main__':
    Main()