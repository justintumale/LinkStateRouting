import socket
import echomessage
import json
import ClientListener


class EchoClient:
    '''
    A client that communicates with the router and may send/receive echo messages to other
    nodes in the network.
    '''
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

    def run(self):
        '''Prompts users for input and sends input.  It also listens for incoming
        messages using the ClientListener thread.'''
        print("First enter the message.  Then enter the recipient's node name.")
        print("To quit, type 'quit'.")
        message = input('->')
        recipient = input('to node: ')

        echo_message = echomessage.EchoMessage('fjt14188', recipient, message)
        json_echo_message = json.dumps(echo_message.__dict__)

        client_listener = ClientListener.ClientListener(self.socket)
        client_listener.start()

        while True:
            self.socket.sendto(json_echo_message.encode('utf-8'), self.router)  #send a message to Router's 50021 port
            message = input('->')
            if message == 'quit':           #if message is 'quit', close the listener thread and break the while loop
                client_listener.flag = False
                break
            recipient = input('to node: ')
            echo_message = echomessage.EchoMessage('fjt14188', recipient, message)  #construct an echo message from
            json_echo_message = json.dumps(echo_message.__dict__)                   #user input and dump in dictionary

        print('Goodbye.')
        client_listener.join()
        self.socket.close()

def Main():
    '''Creates an instance of the EchoClient class and runs it.'''
    client = EchoClient()
    client.run()

if __name__ == '__main__':
    Main()