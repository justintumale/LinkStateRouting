import threading
import OverlayGraph
import time

class OverlayGraphMonitor(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        G = OverlayGraph.OVERLAY_GRAPH
        for key in G:
            #select an entry from the graph
            if len(G[key]) != 0:
                for i in range(0, len(G[key])-1):
                    #if a link from that entry has expired, delete it
                    if G[key][i].expiration_time - time.time() <= 0:
                        del G[key][i]