from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # self.vertices = {"A": set(), "B": set() }
        self.vertices[vertex_id] = set()
        # list: []
        # tuple: ()
        # set - cross between a dictionary and a list. Can iterate through it like a list (has constant time lookup). {1, 2, 3}

        # Can mutate a list, but a tuple is immutable.

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # check to see if vertices exist
        # if they do exist
        if v1 in self.vertices and v2 in self.vertices:
            v1_edges_set = self.vertices[v1]
            v1_edges_set.add(v2)
            # self.vertices = {"A": set("B"), "B": set() } - adding v2 to v1
            # if adding undirected edge, would have to add both ways, but this one is directed v1 -> v2
            # v2_edges_set = self.vertices[v2]
            # v2_edges_set.add(v1)
        # if vertices dont exist
        else:
            raise ValueError("vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # check to see if vertex exists
        # if they do exist
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
            # vertex id of "A" would return set("B")
        # if vertices dont exist
        else:
            raise ValueError("vertex does not exist")

    # Breadth first - use queue, FIFO

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # MEMORIZE THIS ALGORITHM :)
        # Create an empty queue
        q = Queue()
        # Enqueue the starting_vertex
        q.enqueue(starting_vertex)
        # Create an empty set to store visited vertices - using set instead of array b/c no duplicates and O(1) lookup instead of O(n)
        visited = set()
        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the first vertex (becomes our current vertex)
            current_vertex = q.dequeue()
        # Check if its been visited
            # If it has NOT been visited...
            if current_vertex not in visited:
                # Mark it as visited
                print("current vertex from breadth first = ", current_vertex)
                visited.add(current_vertex)
                # Grab its neighbors
                for neighbor in self.get_neighbors(current_vertex):
                    # Enqueue neighbors to back of queue
                    q.enqueue(neighbor)
        # return visited
        return visited

        # prints out 1,2,3,4,5,6,7
        # Example:
        # q = Queue (4)
        # visited = set(1,2,3)
        # current_node = 3
        # neighbors = set(5)

    # Depth first - use stack, LIFO

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack
        s = Stack()
        # Push the starting vertex onto stack
        s.push(starting_vertex)
        # Create an empty set to store visited vertices
        visited = set()
        # While the stack is not empty
        while s.size() > 0:
            # Pop off whats on top (becomes our current vertex)
            current_vertex = s.pop()
            # Check if its been visited
            # If it hasnt been visited...
            if current_vertex not in visited:
                # Mark it as visited
                print("current vertex from depth first = ", current_vertex)
                visited.add(current_vertex)
                # Grab current vertex's neighbors
                for neighbor in self.get_neighbors(current_vertex):
                    # Push all of its neighbors onto the stack
                    s.push(neighbor)

        # return visited
        return visited

        # prints out 1,2,4,7,6,3,5

    # can only do depth first recursively, cant do breadth first
    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        # BASE CASE: No neighbors left to visit
        # Check if the vertex has been visited
        if starting_vertex not in visited:
            # If not...
            # Mark vertex as visited
            print("starting vertex from dft_recursive = ", starting_vertex)
            visited.add(starting_vertex)
            # Call dft_recursive on each neighbor (RECURSIVE CASE)
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

        return visited

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue
        q = Queue()
        # Enqueue a PATH to the starting vertex. Since its a path, order does matter ex. path = [1, 2]
        q.enqueue([starting_vertex])
        # Create an empty set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the path, this is our current path
            current_path = q.dequeue()
            # Grab vertex from the end of our current path, this is our current vertex
            current_vertex = current_path[-1]           
            # Check if its the target
            if current_vertex == destination_vertex:
                # if it is the target, return the current PATH
                return current_path
            # Check if we have visited this vertex before
            # If it hasnt been visited..
            if current_vertex not in visited:
                # Mark it as visited
                print("vertex from bfs = ", current_vertex)
                visited.add(current_vertex)
                # Enqueue a PATH to all of its neighbors...
                for neighbor in self.get_neighbors(current_vertex):
                    # Make each neighbor its own copy of the path - arrays are passed by reference, so we need to make a copy of it first
                    path_copy = current_path.copy() # could also do current_path[:]
                    path_copy.append(neighbor)
                    # Enqueue the copy
                    q.enqueue(path_copy)

            # prints 1,2,4,6
            # example...
            # q = Queue([1,2])
            # visited = set()
            # current_path = [1]
            # current_node = 1
            # neighbors = set(2)
            # path_copy = [1,2]  -> current_path, neighbor   

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
                print("vertex from dfs = ", vertex)
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
    # can only do depth first recursively, cant do breadth first
    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)
            if starting_vertex == destination_vertex:
                return path_copy
            for neighbor in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, path_copy)
                if new_path is not None:
                    return new_path
        return None


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
