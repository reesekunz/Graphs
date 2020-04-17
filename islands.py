islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
​
​
big_islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
               [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
               [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
               [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
               [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
               [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
               [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]
​
# Graph terminology:
# Nodes: 1s
# Edges: s, e, n, w
# What is an island? Connected components
​


def getNeighbors(node, islands):
    row, col = node


​
   neighbors = []
    stepNorth = stepSouth = stepEast = stepWest = False
​
   if row > 0:
        stepNorth = row - 1
​
   if col > 0:
        stepWest = col - 1
​
   if row < len(islands) - 1:
        stepSouth = row + 1
​
   if col < len(islands) - 1:
        stepEast = col + 1
​
   if stepNorth is not False and islands[stepNorth][col]:
        neighbors.append((stepNorth, col))
    if stepSouth is not False and islands[stepSouth][col]:
        neighbors.append((stepSouth, col))
    if stepWest is not False and islands[row][stepWest]:
        neighbors.append((row, stepWest))
    if stepEast is not False and islands[row][stepEast]:
        neighbors.append((row, stepEast))
​
   return neighbors
​


def dft_recursive(node, visited, islands):
    if node not in visited:
        visited.add(node)

​
   neighbors = getNeighbors(node, islands)
    for neighbor in neighbors:
        dft_recursive(neighbor, visited, islands)
​
​


def island_counter(islands):
    visited = set()
    total_islands = 0
# iterate across the matrix
    for row in range(len(islands)):
        for col in range(len(islands)):
            node = (row, col)

​
          # when we hit a 1, if not visited, run a dft/bft
   if islands[row][col] == 1 and node not in visited:
        total_islands += 1
          # mark all nodes in our connected component aka island as visited
        dft_recursive(node, visited, islands)
​
# increment a counter
   return total_islands
​
# should be 4, and 13
print(island_counter(islands))
print(island_counter(big_islands))
