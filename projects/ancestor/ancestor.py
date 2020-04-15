class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = set()

    def add_edge(self, child, parent):
        self.nodes[child].add(parent)

    def getNeighbors(self, child):
        return self.nodes[child]


class Stack:
    def __init__(self):
        self.storage = []

    def pop(self):
        return self.storage.pop()

    def push(self, item):
        self.storage.append(item)

    def size(self):
        return len(self.storage)


# 3 steps to solve any graphs problem:

# 1. Describe in terms of graphs.
# Nodes: People
# Edges: Connected if they're parent-child

# 2. Build our graph
# Two choices:
# Build a graph class
# Don't write an adjacency list or matrix, just a getNeighbors()


# 3. Choose a graph algorithm:
# Traversal or search? Traversal b/c we want to visit all the nodes to find the earliest ancestor. No particular node at which well just stop.
# Breadth or depth? Depth. But it really only matters if its a search. Traversal has same time complexity for both.

# Tracking distance with each node as you go
def dft(starting_node, graph):
    stack = Stack()

    stack.push((starting_node, 0))

    visited = set()

    visited_pairs = set()

    while stack.size() > 0:
        current_pair = stack.pop()
        visited_pairs.add(current_pair)
        current_node = current_pair[0]
        current_distance = current_pair[1]

        if current_node not in visited:
            visited.add(current_node)

            parents = graph.getNeighbors(current_node)

            for parent in parents:
                parent_distance = current_distance + 1
                stack.push((parent, parent_distance))

    longest_distance = 0
    earliest_one = -1
    for pair in visited_pairs:
        node = pair[0]
        distance = pair[1]
        if distance > longest_distance:
            longest_distance = distance
            earliest_one = node
    return earliest_one


# [(1,3), (2,3), (3,6), (5,6), (5,7), (4,5), (4,8), (8,9), (11,8), (10,1) ]
def earliest_ancestor(ancestors, starting_node):
    # Build our graph
    graph = Graph()
    for parent, child in ancestors:
        graph.add_node(child)
        graph.add_node(parent)
        graph.add_edge(child, parent)

    # Run DFT
    earliest_one = dft(graph, starting_node)

    # Choose the longest path (most distant ancestor)
    # Run DFT but track each path, then choose the longest path
    return earliest_one
