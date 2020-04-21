from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from util import Stack, Queue
# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# The maze is known (we could run DFT on it)
# The step-by-step path is unknown (we must build on top of the DFT algorithm). Keep track of the extra information ourselves (backtrack)

# When randomly picking a starting point.
# Is it a valid exit?
# Make sure its not where you came from.

# Fill this out with directions to walk
# when walked in order, will visit every room on the map at least once.
# May find the commands player.current_room.id, player.current_room.get_exits(), and player.travel(direction) useful.
# Cant just use a traversal algorithm b/c need to backtrack. Cant just go from 2 back to 0 b/c need to physically go from room 2 - room 1 - 0.
# Need to keep track of the path we took to get there so can take that path backwards
#

# traversal_path = []
# player.current_room.get_exits() => return ['n','s','e','w'] since 0 is right in the middle
# player.travel(south)
# call player.current_room.id to see which room id south is (room 5).
# call player.current_room.get_exits() => returns which directions you can go in now from room 5.
# {
#   0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
#   5: {'n': 0, 's': '?', 'e': '?'}
# }
# Filling out graph as we go from room to room.

# 0 -> 3 -> 4
# my_graph = {0: {'n': "?", "s": "?", "e": 3, "w": "?"},
#             3: {"w": 0, "e": 4, 4: {"w": 3}}}

# Once we get to room 4, we need to break out of DFT w/ While Loop. This is b/c we have to backtrack through room 3 but a DFT would just jump back to 0.
# From 4, we use a BFS to find the shortest path back to 0. player.current_room = 4. Run BFS, searching for a '?', which is an unexplored room.
# Path from [4,3]. Mark 4 as visited. Then go from [3,0]. 0 has a '?'.
# Once you found the ?, ready to run a DFS again. DFS will choose unexplored exit and start making its way down a path until no more '?'.

print("current room = ", player.current_room)
print("current room id = ", player.current_room.id)
print("current_room.get_exits() = ", player.current_room.get_exits())
print("player travel direction = ", player.travel('n'))

traversal_path = ['n', 'n']
for x in traversal_path:
    print(x)

# Start by writing an algorithm that picks a random unexplored direction from the player's current room, travels and logs that direction, then loops. This should cause your player to walk a depth-first traversal. When you reach a dead-end(i.e. a room with no unexplored paths), walk back to the nearest room that does contain an unexplored path.
random_direction = random.choice(['n', 's', 'e', 'w'])
print('random_direction', random_direction)
if random_direction == 's':
    player.travel('s')
    print(player.current_room)
elif random_direction == 'n':
    player.travel('n')
    print(player.current_room)
elif random_direction == 'w':
    player.travel('w')
    print(player.current_room)
elif random_direction == 'e':
    player.travel('e')
    print(player.current_room)

    # DFT
    # Explore the graph in one direction
    # As we go, log our directions in our traversal path (add to our traversal path)
    # BFS
    # When we hit a dead end, find the nearest unexplored room (room with a '?)
    # As we go to the nearest unexplore room, log our path again (w, w)
    # Break and go back to DFT
    # Repeat until all rooms are visited

    # Things to think about
    # When you move into a room, update the previous room. Previous room will now have the id of the direction you went
    # Exiting DFT and running BFS
    # When you find a ?, stop DFS and run DFT
    # Convert BFS PATH into directions for your traversal_path

    # traversal_path = ['e', 'e', 'w',  'w']

    # Note: BFS will return the path as a list of room IDs. You will need to convert this to a list of n/s/e/w directions before adding it to the traversal path.

    # room_id = player.current_room.id

    # if room_id not in my_graph:
    #     # adding a dictionary inside of a dictionary. grabbing whatever is inside the room_id and making its value a dictionary.
    #     my_graph[room_id] = {}

    # room_exits = player.current_room.get_exits()
    # ['n', 's', 'e', 'w']
    # Accessing a nested dictionary
    # for exit in exits:
    #     my_graph[room_id][exit] = '?'

    # Why do we have to start by picking a random unexplored direction?
    # B/c we dont know whats in the maze and have to build our own map of the maze as we go. If we randomize it each time, we have better odds of finding the shortest possible path through the maze compared to if we just started at 0 each time.

    # room_exits = player.current_room.get_exits()
    # next_direction = random.randint(0, len(room_exits) -1)

    # TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
