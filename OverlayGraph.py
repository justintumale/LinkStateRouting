from pprint import pprint

class LiveNode:
    node_name = ''
    expiration_time = -1
    live = False
    def __init__(self, node_name, expiration_time):
        self.node_name = node_name
        self.expiration_time = expiration_time
        if self.expiration_time > 0:
            self.live = False



OVERLAY_GRAPH = {'student0' : [],
                'kbadams'   : [],
                'jadolphe'  : [],
                'cannan'    : [],
                'mbamaca'   : [],
                'adb2016'   : [],
                'bbreyel'   : [],
                'derosa30'  : [],
                'ddiener'	: [],
                'foretich'	: [],
                'coal175'	: [],
                'reiner'	: [],
                'ahayes44'	: [],
                'ahiggins'	: [],
                'da3nvy'	: [],
                'yd9'	    : [],
                'hjink94'	: [],
                'stevenk'	: [],
                'bruceli'	: [],
                'mattling'	: [],
                'erlock'	: [],
                'alexms'	: [],
                'brandonm'	: [],
                'jarmac76'	: [],
                'kamercer'	: [],
                'dylmorg'	: [],
                'nikolich'	: [],
                'mbp1988'	: [],
                'lpastor'	: [],
                'rpersaud'	: [],
                'jplizzle'	: [],
                'tonyr'	    : [],
                'mreece05'	: [],
                'rucker21'	: [],
                'quintezs'	: [],
                'jls93'	    : [],
                'kds'	    : [],
                'trsturbo'	: [],
                'fjt14188'	: [],
                'lvanhuss'	: [],
                'lucyv'	    : [],
                'vinsonj'	: [],
                'jakewebb'	: [],
                'whatleym'	: [],
                'wilbur13'	: [],
                'mwong9'	: [],
                'byang9'	: [],
                'dilawarz'	: []}


def create_link(from_node, to_node, expiration):
    global OVERLAY_GRAPH
    if len(OVERLAY_GRAPH[from_node]) == 0:
        link = LiveNode(to_node, expiration)
        OVERLAY_GRAPH[from_node].append(link)

    else:

        for i in range(0, len(OVERLAY_GRAPH[from_node])):
            if to_node != OVERLAY_GRAPH[from_node][i]:
                pass
            else:
                del OVERLAY_GRAPH[from_node][i]
                OVERLAY_GRAPH[from_node].append(LiveNode(to_node, expiration))
                break
            OVERLAY_GRAPH[from_node].append(LiveNode(to_node, expiration))


OVERLAY_GRAPH['fjt14188'].append(LiveNode('mwong9', 9000))
OVERLAY_GRAPH['fjt14188'].append(LiveNode('dylmorg', 9000))
create_link('fjt14188', 'lucyv', 9000)


for key in OVERLAY_GRAPH:
    print(key, end=': ')
    for links in OVERLAY_GRAPH[key]:
        print(links.node_name, end=' ')
    print()

