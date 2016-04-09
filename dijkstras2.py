import OverlayGraph
class Node():
    def __init__(self, name, connections=None):
        self.name = name
        self.connections = {}
        if connections is not None:
            self.connections.update(connections)


graph = OverlayGraph.OVERLAY_GRAPH
OverlayGraph.create_link('fjt14188', 'mbamaca', 10000)
OverlayGraph.create_link('mbamaca', 'cannan', 10000)
OverlayGraph.create_link('fjt14188', 'jadolphe', 10000)
OverlayGraph.create_link('jadolphe', 'coal175', 10000)
OverlayGraph.create_link('coal175', 'cannan', 10000)

OverlayGraph.print_graph()



def neighbors(graph, root, branch):
    for link in graph[root]:
        if link.name == branch:
            return True
    return False

print(neighbors(graph, 'fjt14188', 'mbamaca'))


#list = []
#def dijkstras():
#    list.append(graph['fjt14188'])
#    for key in graph:


        #if neighbors(graph, graph[node], graph['fjt14188']):
        #    node.weight = 1
        #else:
        #    node.weight = 9999


#dijkstras()








