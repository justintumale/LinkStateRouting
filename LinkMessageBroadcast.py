import threading

class LinkMessageBroadcast(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print('Running Broadcaster...')
