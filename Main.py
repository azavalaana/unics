# Lab 3 Option B
# Antonio Zavala

import time
from AVLNode import Node
from AVLTree import AVLTree
from RBNode import RBTNode
from RBTree import RedBlackTree


# Create AVL tree from given file
def create_avl_tree(file_name):
    english_words = AVLTree()

    # Open file and read first line
    file = open(file_name, "r")
    line = file.readline()

    # Loop to read all lines in the file
    while line:
        # Add each word from the list
        new_word = Node(line.rstrip().lower())
        english_words.insert(new_word)
        line = file.readline()

    return english_words


# Creates a Red-Black tree from given file
def create_rb_tree(file_name):
    english_words = RedBlackTree()

    # Open file and read first line
    file = open(file_name, "r")
    line = file.readline()

    # Loop to read all lines in the file
    while line:
        # Add each word from the list
        english_words.insert(line.rstrip().lower())
        line = file.readline()

    return english_words


# Method to print whole tree
def print_tree(tree_node):
    if tree_node is None:
        print("Your tree is empty.")
        return
    # Print left sub-tree
    if tree_node.left is not None:
        print_tree(tree_node.left)
    print(tree_node.key)
    # Print right sub-tree
    if tree_node.right is not None:
        print_tree(tree_node.right)


# method that generates all permutations from a word
def get_perms(word):
    if len(word) <= 1:
        return word
    else:
        perm_list = []
        for perm in get_perms(word[1:]):
            for i in range(len(word)):
                perm_list.append(perm[:i] + word[0:1] + perm[i:])
        return perm_list


# Method that prints all valid anagrams from a given word
def print_anagrams(word, tree):
    permutations = get_perms(word)

    for i in range(len(permutations)):
        if tree.search(permutations[i]):
            print(permutations[i])
    return


# Method that returns the number of valid anagrams from a given word
def count_anagrams(word, tree):
    permutations = get_perms(word)
    count = 0

    for i in range(len(permutations)):
        if tree.search(permutations[i]):
            count += 1

    return count


def main():
    start_time = time.time()
    avl_tree = create_avl_tree("words.txt")
    print("--- %s seconds ---" % (time.time() - start_time))
    print_tree(avl_tree.root)
    print(count_anagrams(word, avl_tree))

    start_time = time.time()
    rb_tree = create_rb_tree("words.txt")
    print("--- %s seconds ---" % (time.time() - start_time))
    print_tree(rb_tree.root)
    print(count_anagrams(word, rb_tree))

    main()