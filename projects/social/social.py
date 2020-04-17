import random
import time
​
class Queue:
    def __init__(self):
        self.storage = []
​
    def enqueue(self, item):
        self.storage.append(item)
​
    def dequeue(self):
        return self.storage.pop(0)
​
    def size(self):
        return len(self.storage)
​
class User:
    def __init__(self, name):
        self.name = name
​
class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
​
    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
​
    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()
​
    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
​
        Creates that number of users and a randomly distributed friendships
        between those users.
​
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
​
        # Add users
        for user in range(num_users):
            self.add_user(user)
​
    # create a list with all possible friendship combinations
        friendships = []
        for user in range(1, self.last_id + 1):
            for friend in range(user + 1, num_users):
                friendships.append((user, friend))
​
    # shuffle the list,
        # mutate in place with: random.shuffle(array)
​
        # or, Fisher-Yates shuffle!
        for idx in range(len(friendships)):
         # randint will give us an integer in this range, inclusive (includes last number)
            rand_idx = random.randint(0, len(friendships) - 1)
            # I think this syntax for swapping items is sweet
            friendships[idx], friendships[rand_idx] = friendships[rand_idx], friendships[idx]
​
    # then grab the first N elements from the list.
        total_friendships = num_users * avg_friendships
        pairs_needed = total_friendships // 2 # because add_friendship makes two at a time
        random_friendships = friendships[:pairs_needed]
​
        # Create friendships
        for friendship in random_friendships:
            self.add_friendship(friendship[0], friendship[1])
​
            # Sammy's idea
# just keep getting "random" friendships and if they've already been added,
# just find another pair?
# just run til we hit required # of friendships
​
    def populate_graph_linear(self, num_users, avg_friendships):
        # Reset graph
        self.friendships = {}
        self.users = {}
        self.last_id = 0
​
        # add all users
        for user_id in range(num_users):
            self.add_user(user_id)
​
        total_friendships = num_users * avg_friendships
​
        friendships_made = 0
​
        failures = 0
​
        while friendships_made < total_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
​
            if user_id != friend_id and friend_id not in self.friendships[user_id]:
                self.add_friendship(user_id, friend_id)
                friendships_made += 1
            else:
                failures += 1
​
        print(failures)
​
​
​
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument
​
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
​
        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
​
        q = Queue()
        path = [user_id]
        q.enqueue(path)
​
        while q.size() > 0:
            current_path = q.dequeue()
            current_user = current_path[-1]
​
            if current_user not in visited:
                visited[current_user] = current_path
​
                friends = self.friendships[current_user]
​
                for friend in friends:
                    path_copy = current_path[:]
                    path_copy.append(friend)
                    q.enqueue(path_copy)
​
        return visited
​
​
if __name__ == '__main__':
    sg = SocialGraph()
    # print(sg.friendships)
    # print(sg.friendships[1])
    # connections = sg.get_all_social_paths(1)
    # print(len(connections) - 1)
​
    # total_paths = 0
    # for friend_id in connections:
    #     friend_path = connections[friend_id]
    #     total_paths += len(friend_path)
    # average_path_length = total_paths / len(connections)
​
    # print(f"Average path length: {average_path_length}")
​
    num_users = 2000
    avg_friendships = 500
​
    start_time = time.time()
    sg.populate_graph(num_users, avg_friendships)
    end_time = time.time()
​
    print(f"Quadratic run time: {end_time - start_time}")
​
    start_time = time.time()
    sg.populate_graph_linear(num_users, avg_friendships)
    end_time = time.time()
​
    print(f"Linear run time: {end_time - start_time}")