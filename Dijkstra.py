import OverlayGraph
import math
import time
import queue
import pprint
import threading

'''class Node():
    def __init__(self, name, connections=None):
        self.name = name
        self.connections = {}
        if connections is not None:
            self.connections.update(connections)
'''
'''
overlay_graph = OverlayGraph.OVERLAY_GRAPH
OverlayGraph.create_link('fjt14188', 'mbamaca', 10000)
OverlayGraph.create_link('mbamaca', 'cannan', 10000)
OverlayGraph.create_link('fjt14188', 'jadolphe', 10000)
OverlayGraph.create_link('jadolphe', 'coal175', 10000)
OverlayGraph.create_link('coal175', 'cannan', 10000)
OverlayGraph.create_link('cannan', 'mwong9', 10000)
OverlayGraph.create_link('fjt14188', 'adb2016', 10000)
OverlayGraph.create_link('adb2016', 'derosa30', 10000)
OverlayGraph.create_link('derosa30', 'bbereyel', 10000)
OverlayGraph.create_link('mwong9', 'reiner', 10000)
OverlayGraph.create_link('bbreyel', 'reiner', 10000)

#OverlayGraph.print_graph()
'''''

every_node = []
node_weight_map = {}
node_parent_map = {}
not_visited = []
priority_queue = queue.PriorityQueue(60)
visited_set = []

def initialize_weights(overlay_graph, node_weight_map, root):
    '''
    Initialize the weights on the node_weight_map to infinity except for
    the root.
    :param overlay_graph: the overlay graph
    :param node_weight_map: the hashmap that maps nodes to their weights
    :param root:    the root node
    :return:
    '''
    node_weight_map[root] = root
    #infinity = math.inf <---- does not work on vm420
    infinity = 9999
    visited_set.append(root)
    for key in overlay_graph:   #append the key to the list of all nodes
        every_node.append(key)
        if key == root:         #if the key is the root, set its weight to 0
            node_weight_map[key] = 0
        else:
            node_weight_map[key] = infinity #if not the root, set to infinity
            not_visited.append(key)


def check_if_neighbors(overlay_graph, root, branch):
    '''
    Check if two nodes are neighbors
    :param overlay_graph: the overlay graph
    :param root:    the root node
    :param branch:  the node to check if its a neighbor of the root
    :return:    True if the two nodes are neighbors
    '''
    for link in overlay_graph[root]:
        #if the link connected to the root in the graph is equal to the branch
        #then return true
        if link.name == branch:
            return True
    return False


def find_not_visited_neighbors(overlay_graph, node, not_visited):
    '''

    :param overlay_graph: the overlay graph
    :param node: the current node who's neighbors were checing for
    :param not_visited: the list of unvisited nodes
    :return:
    '''
    neighbors = []
    for key in not_visited:
        if check_if_neighbors(overlay_graph, node, key):
            neighbors.append(key)
        else:
            pass
    return neighbors

def relax_neighbors(node, overlay_graph):
    '''
    If the sum of weight of the current node and the path to get to the neighbor
    is less than the neighbor's current weight, then change the neighbor's
    current weight to the sum.
    :param node:    the current node
    :param overlay_graph:   the overlay graph
    '''
    neighbors = find_not_visited_neighbors(overlay_graph, node, not_visited)
    #neighbors = find_neighbors(overlay_graph, node)
    for neighbor in neighbors:
        if (node_weight_map[neighbor] >= node_weight_map[node] + 1):
            node_weight_map[neighbor] = node_weight_map[node] + 1
            node_parent_map[neighbor] = node
        priority_queue.put((node_weight_map[neighbor], neighbor))


def find_shortest_path(node_parent_map, root, destination, splist):
    '''
    After Dijkstra's algorithm creates the graph that contains the shortest
    path from the root to all nodes, this algorithm will find the shortest
    path from the destination node back to the root node.

    :param node_parent_map: the hashmap that maps nodes to their parent node according to
        the shortest paths from the root
    :param root: the root node
    :param destination: the destination node
    :param splist: the list that will contain the shortest path
    :return:
    '''
    if destination == root:
        splist.append(root)
        #print('this is the unreturned path', a)
        return splist
    else:
        splist.append(destination)
        return find_shortest_path(node_parent_map,root, node_parent_map[destination], splist)



def dijkstras(root, destination, overlay_graph ):
    '''
    Dijkstra's algorithm that finds the shortest path from the root node
    to a destination node.
    :param root: the root node
    :param destination: the destination node
    :param overlay_graph: the overlay graph
    :return: the shortest path from the root to the destination
    '''
    #1 start at root
    #2 push node to visited
    #3 find node's neighbors
    #4 relax all neighbors
    #5 push all the neighbors to the priority queue
    #6 visit the neighbor with the lowest weight
    #7 repeat steps 2 - 7 until destination has been pushed to visited


    initialize_weights(overlay_graph, node_weight_map, 'fjt14188')
    relax_neighbors(root, overlay_graph)

    path_available = True
    while True:
        if priority_queue.empty():
            print('breaking')
            path_available = False
            break
        node = priority_queue.get()[1]          #set the current node as the first item in the queue
        #push node to visited
        visited_set.append(node)                #add the node to the visited list
        #remove node from not_visited list
        if node in not_visited:
            not_visited.remove(node)            #remove the node from the not-visited list
        relax_neighbors(node, overlay_graph)    #relax neighbors & push them to priority queue
        if destination in visited_set:          #if the destination is in the visited set, exit
            break

    if path_available:
        list = []
        shortest_path = find_shortest_path(node_parent_map, root, destination, list)
        shortest_path.reverse()  #find_shortest_path returns a list from destination --> root, so reverse
        return(shortest_path)
    else:
        return

'''
pp = pprint.PrettyPrinter(indent=4)
print('calculating shortest path...')
print(dijkstras('fjt14188', 'reiner'))

pp.pprint(node_weight_map)
print()
pp.pprint(node_parent_map)
'''

