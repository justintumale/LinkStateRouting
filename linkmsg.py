import json, time

class LinkMsg:
    '''LinkStateMessage, reconstituted from JSON'''

    def __init__(self, fromNode = None, toNode=None) :
        self.fromNode   = fromNode
        self.toNode     = toNode
        self.expiration = int(time.time())+120 

    def reconstitute_(self, jsonText):
        '''Reconstitute this message from JSON text'''
        self.__dict__ = json.loads(jsonText)

if __name__ == "__main__":
    #demo JSON encoding
    msg = LinkMsg('salida','aspen')
    jsonText = json.dumps(msg.__dict__)
    print ('Json Encoding: '+jsonText)
    newMsg= LinkMsg()
    #newMsg.reconstitute(jsonText)
    dict = json.loads(jsonText)
    print ('Reconstituted message: from: '+dict['fromNode'] +' to: '+dict['toNode'] + ' expires: '+str(dict['expiration']))



