import socket
import echomessage
import json
import ClientListener


class EchoClient:
    host = ''
    port = ''
    socket = ''
    router = ''

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 5002
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.host, self.port))

        self.router = (self.host, 24721) #router port

    def send_echo(self):
        '''Sends an echo message to the LSRouter'''
        pass

    def receive_echo(self):
        '''Receives an echo message from the LSRouter'''
        pass

    def run(self):
        print("First enter the message.  Then enter the recipient's node name.")
        print("To quit, type 'quit'.")
        message = input('->')
        recipient = input('to node: ')

        echo_message = echomessage.EchoMessage('fjt14188', recipient, message)
        json_echo_message = json.dumps(echo_message.__dict__)

        client_listener = ClientListener.ClientListener(self.socket)
        client_listener.start()

        while message is not 'quit':
            self.socket.sendto(json_echo_message.encode('utf-8'), self.router)  #send a message to Router's 50021 port

            message = input('->')
            recipient = input('to node: ')
            echo_message = echomessage.EchoMessage('fjt14188', recipient, message)
            json_echo_message = json.dumps(echo_message.__dict__)

        client_listener.join()
        self.socket.close()


def Main():
    client = EchoClient()
    client.run()

if __name__ == '__main__':
    Main()