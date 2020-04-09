"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            # if adding undirected edge would have to add both ways, but this one is directed v1 -> v2
            # self.vertices[v1].add(v2)
            # self.vertices[v2].add(v1)
        else:
            # print("ERROR: vertex does not exist").. same as
            raise ValueError("vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
             # print("ERROR: vertex does not exist").. same as
            raise ValueError("vertex does not exist")

    # Breadth first - use queue, FIFO
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # MEMORIZE THIS ALGORITHM :)
        # Create a queue
        q = Queue()
        # Enqueue the starting vertex
        q.enqueue(starting_vertex)
        # Create a set to store visited vertices - using set instead of array b/c no duplicates and O(1) lookup instead of O(n)
        visited = set()
        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the first vertex
            vertex = q.dequeue()
        # Check if its been visited
            # If it has NOT been visited...
            if vertex not in visited:
                # Mark it as visited
                print("vertex from breadth first = ", vertex)
                visited.add(vertex)
                # Enqueue all of its neighbors to back of queue
                for neighbor in self.get_neighbors(vertex):
                    q.enqueue(neighbor)

        # prints out 1,2,3,4,5,6,7

    # Depth first - use stack, LIFO
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack
        s = Stack()
        # Push the starting vertex
        s.push(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the stack is not empty
        while s.size() > 0:
            # Pop the first vertex
            vertex = s.pop()
            # Check if its been visited
            # If it hasnt been visited...
            if vertex not in visited:
                # Mark it as visited
                print("vertex from depth first = ", vertex)
                visited.add(vertex)
            # Push all of its neighbors onto the stack
            for neighbor in self.get_neighbors(vertex):
                s.push(neighbor)

            # prints out 1,2,4,7,6,3,5

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        # Check if the vertex has been visited (BASE CASE)
        if starting_vertex not in visited:
            # If not...
            # Mark vertex as visited
            print("starting vertex from dft_recursive = ", starting_vertex)
            visited.add(starting_vertex)
            # Call dft_recursive on each neighbor (RECURSIVE CASE)
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue
        q = Queue()
        # Enqueue a PATH to the starting vertex. Since its a path, order DOES matter
        q.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # GRAB VERTEX FROM END OF THE PATH
            vertex = path[-1]
            # Check if its been visited
            # If it hasnt been visited..
            if vertex not in visited:
                # Mark it as visited
                visited.add(vertex)
                # Check if its the target
                if vertex == destination_vertex:
                    # if it is the target, return the PATH
                    return path
                # Enqueue a PATH to all of its neighbors...
                for neighbor in self.get_neighbors(vertex):
                    # Make a copy of the path - arrays are passed by reference, so we need to make a copy of it first
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    # Enqueue the copy
                    q.enqueue(path_copy)

            # prints 1,2,4,6

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        # Create a stack
        s = Stack()
        # Push a PATH to the starting vertex. Since its a path, order DOES matter
        s.push([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while s.size() > 0:
            # Pop the first PATH
            path = s.pop()
            # GRAB VERTEX FROM END OF THE PATH
            vertex = path[-1]
            # Check if its been visited
            # If it hasnt been visited..
            if vertex not in visited:
                # Mark it as visited
                visited.add(vertex)
                # Check if its the target
                if vertex == destination_vertex:
                    # if it is the target, return the PATH
                    return path
                # Enqueue a PATH to all of its neighbors...
                for neighbor in self.get_neighbors(vertex):
                    # Make a copy of the path - arrays are passed by reference, so we need to make a copy of it first
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                # Push the copy
                s.push(path_copy)


        # prints out 1,2,4,7,6 
        
    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
