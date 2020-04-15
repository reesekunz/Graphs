# Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
# Note:
# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin_word and end_word are non-empty and are not the same.

# Sample:
# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']
# begin_word = "sail"
# end_word = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
# beginWord = "hungry"
# endWord = "happy"
# None

# step 1: define the problem in terms of graphs
## what are your nodes? edges (when are two nodes connected)?
## word: node
## hit -> hot
## edge: two words that differ by only 1 letter
## shortest transformation sequence: shortest path, aka BFS
​
# Step 2: build your graph or define getNeighbors function
## the words list is very large
## add words as nodes - maybe only those of same length as our start_word and end_word
## load edges
​
# My thought was comparing letters and trying to tree from hit > cog comparing each letter of the final into the initial and check the word list
# hit > h > c, o ,g >> cit, oit, git
​
## What if, when we want to find a word's neighbors, we swapped out every letter of the alphabet for each letter of the word?
## Would that give us all the neighbors of hit?
## What would be the time complexity? finding neighbors of this word would be linear in length of word
​
import string
from util import Queue
alphabet = string.ascii_lowercase
​
file = open('words.txt', 'r')
words = file.read().split('\n')
file.close()
​
word_set = set()
for word in words:
    word_set.add(word.lower())
​
def getNeighbors(word):
    # make an empty list to hold the neighbors
    neighbors = []
    # for each letter in the word:
    for i in range(len(word)):
        letter = word[i]
    ## for each letter of the alphabet
        for alpha_letter in alphabet:
            # turn the word into a list
            word_list = list(word)
            ### swap the word-letter with the alphabet-letter
            word_list[i] = alpha_letter
            # turn word back into string
            maybe_neighbor = "".join(word_list)
            ### check if the new word is in our word list
            if maybe_neighbor in word_set and maybe_neighbor != word:
                neighbors.append(maybe_neighbor)
                ### if so, add it to our list of neighbors
​
    # return the list of neighbors
    return neighbors
​
# step 3: choose and run your algorithm
## choose BFS
​
def bfs(start_word, end_word):
    q = Queue()
    visited = set()
​
    path = [start_word]
    q.enqueue(path)
​
    while q.size() > 0:
        current_path = q.dequeue()
​
        current_word = current_path[-1]
​
        if current_word == end_word:
            return current_path
​
        if current_word not in visited:
            visited.add(current_word)
​
            neighbors = getNeighbors(current_word)
​
            for neighbor in neighbors:
                path_copy = current_path[:]
                path_copy.append(neighbor)
                q.enqueue(path_copy)
​
print(bfs('hit', 'cog'))
print(bfs('sail', 'boat'))
print(bfs('hungry', 'happy'))