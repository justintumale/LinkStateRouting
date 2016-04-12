import json
class EchoMessage():
    '''Represents a message in form From:<from> To:<to> Message: <msg>,
    where 'from' and 'to' are node names'''

    def __init__(self,from_node,to_node,message):
        '''Load input paramsinto message fields'''
        self.from_node =from_node
        self.to_node   = to_node
        self.msg       = message

if __name__ == '__main__':
    msg = EchoMessage('Starfleet','Spacedock','Launch all vessels')
    jsonText = json.dumps(msg.__dict__)
    print ('Json Encoding: '+jsonText)


    data = json.loads(jsonText)
    print('DATA', data)
    print(data['from_node'])
