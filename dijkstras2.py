import OverlayGraph
import math
import time
import queue
import pprint

class Node():
    def __init__(self, name, connections=None):
        self.name = name
        self.connections = {}
        if connections is not None:
            self.connections.update(connections)


overlay_graph = OverlayGraph.OVERLAY_GRAPH
OverlayGraph.create_link('fjt14188', 'mbamaca', 10000)
OverlayGraph.create_link('mbamaca', 'cannan', 10000)
OverlayGraph.create_link('fjt14188', 'jadolphe', 10000)
OverlayGraph.create_link('jadolphe', 'coal175', 10000)
OverlayGraph.create_link('coal175', 'cannan', 10000)
OverlayGraph.create_link('cannan', 'mwong9', 10000)

OverlayGraph.print_graph()

every_node = []
node_weight_map = {}
node_parent_map = {}
not_visited = []
priority_queue = queue.PriorityQueue(60)
visited_set = []


def initialize_weights(overlay_graph, node_weight_map, root):
    node_weight_map[root] = root
    infinity = math.inf
    visited_set.append(root)
    for key in overlay_graph:
        every_node.append(key)
        if key == root:
            node_weight_map[key] = 0
        else:
            node_weight_map[key] = infinity
            not_visited.append(key)

def check_if_neighbors(overlay_graph, root, branch):
    for link in overlay_graph[root]:
        if link.name == branch:
            return True
    return False

def find_not_visited_neighbors(overlay_graph, node, not_visited):
    neighbors = []
    for key in not_visited:
        if check_if_neighbors(overlay_graph, node, key):
            neighbors.append(key)
        else:
            pass
    return neighbors

'''
def find_neighbors(overlay_graph, node):
    neighbors = []
    for key in every_node:
        if check_if_neighbors(overlay_graph, node, key):
            neighbors.append(key)
        else:
            pass
    return neighbors
'''

def relax_neighbors(node):
    neighbors = find_not_visited_neighbors(overlay_graph, node, not_visited)
    #neighbors = find_neighbors(overlay_graph, node)
    for neighbor in neighbors:
        if (node_weight_map[neighbor] >= node_weight_map[node] + 1):
            node_weight_map[neighbor] = node_weight_map[node] + 1
            node_parent_map[neighbor] = node
        #node_weight_map[neighbor] = min(node_weight_map[neighbor], node_weight_map[node] + 1)
        #print('putting', neighbor, node_weight_map[neighbor], 'into the queue...')
        priority_queue.put((node_weight_map[neighbor], neighbor))


def findShortestPath(node_parent_map, root, destination, splist):
    if destination == root:
        splist.append(root)
        #print('this is the unreturned path', a)
        return splist
    else:
        splist.append(destination)
        return findShortestPath(node_parent_map,root, node_parent_map[destination], splist)




def dijkstras(root, destination):
    #1 start at root
    #2 push node to visited
    #3 find node's neighbors
    #4 relax all neighbors
    #5 push all the neighbors to the priority queue
    #6 visit the neighbor with the lowest weight
    #7 repeat steps 2 - 7 until destination has been pushed to visited

    initialize_weights(overlay_graph, node_weight_map, 'fjt14188')
    relax_neighbors(root)
    while True:

        node = priority_queue.get()[1]
        #push node to visited
        visited_set.append(node)
        #remove node from not_visited list
        not_visited.remove(node)
        #relax neighbors & push them to priority queue
        relax_neighbors(node)
        #time.sleep(1)
        if destination in visited_set: break

    print('calculating shortest path...')
    list = []
    shortest_path = findShortestPath(node_parent_map, root, destination, list)
    print('this is the shortest path....', shortest_path)



dijkstras('fjt14188', 'cannan')

pp = pprint.PrettyPrinter(indent=4)
'''
list = []

shortest_path = findShortestPath(node_parent_map, 'fjt14188', 'cannan', list)
print('shortest path! ', shortest_path)
'''

'''
#pp.pprint(node_weight_map)
#print()
pp.pprint(node_parent_map)
'''









