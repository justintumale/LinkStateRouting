import json
class EchoMessage():
    '''Represents a message in form From:<from> To:<to> Message: <msg>,
    where 'from' and 'to' are node names'''

    def __init__(self,fromNode,toNode,message):
        '''Load input paramsinto message fields'''
        self.from_node =fromNode
        self.to_node   = toNode
        self.msg       = message

if __name__ == '__main__':
    msg = EchoMessage('Starfleet','Spacedock','Launch all vessels')
    jsonText = json.dumps(msg.__dict__)
    print ('Json Encoding: '+jsonText)
