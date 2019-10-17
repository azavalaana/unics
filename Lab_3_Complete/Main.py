# Lab 3 Option B
# Antonio Zavala

import time
from AVLNode import Node
from AVLTree import AVLTree
from RBNode import RBTNode
from RBTree import RedBlackTree


# Create AVL tree from given file
def create_avl_tree(file_name):
    try:
        english_words = AVLTree()

        # Open file and read first line
        file = open(file_name, "r")
        line = file.readline()

        if line == "":
            print("Selected file is empty")
            main()

        # Loop to read all lines in the file
        while line:
            # Add each word from the list
            new_word = Node(line.rstrip().lower())
            english_words.insert(new_word)
            line = file.readline()

        return english_words
    except FileNotFoundError:
        print("File not found. Please try again.")
        main()


# Creates a Red-Black tree from given file
def create_rb_tree(file_name):
    try:
        english_words = RedBlackTree()

        # Open file and read first line
        file = open(file_name, "r")
        line = file.readline()

        if line == "":
            print("Selected file is empty")
            main()

        # Loop to read all lines in the file
        while line:
            # Add each word from the list
            english_words.insert(line.rstrip().lower())
            line = file.readline()

        return english_words
    except FileNotFoundError:
        print("File not found. Please try again.")
        main()


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


# Function that returns the word with the most possible anagrams from a given file
def most_anagrams(file_name, tree):
    try:
        if tree.root is None:
            print("Your tree is empty.")
            return None
        # Open file and read first line
        file = open(file_name, "r")
        line = file.readline()

        highest_anagrams = line.rstrip().lower()  # Variable that holds word with most possible anagrams
        highest_count = count_anagrams(highest_anagrams, tree)

        # Loop will go trough every line in the file
        while line:
            new_word = line.rstrip().lower()
            new_count = count_anagrams(new_word, tree)
            if new_count > highest_count:
                highest_anagrams = new_word
                highest_count = new_count
            line = file.readline()

        # Returns word with the most anagrams
        return highest_anagrams
    except FileNotFoundError:
        print("File not found. Please try again.")
        main()


# Main function
def main():
    print("Please select an option: ")
    print()
    print("Type 1 for Binary search using AVL Tree.\nType 2 for Binary search using Red-Black Tree.")
    tree = input("Type 3 to exit program.\n")

    if tree == '1':
        file = input("Please type the name of your file: ")
        print("Please wait while the AVL Tree is generated.")
        start_time = time.time()
        avl_tree = create_avl_tree(file)
        end_time = time.time()
        print("--- %s seconds ---" % (end_time - start_time))
        keep_going = True
        while keep_going:
            print("Please choose an option to perform:")
            print("   1. Print AVL Tree.")
            print("   2. Get the number of anagrams from a word.")
            print("   3. Print all possible anagrams from a word.")
            print("   4. Get the word with the most possible anagrams in a file.")
            answer = input()

            if answer == '1':
                print_tree(avl_tree.root)
            elif answer == '2':
                word = input("Please type the word to search for anagrams: ")
                print(count_anagrams(word, avl_tree))
            elif answer == '3':
                word = input("Please type the word to search for anagrams: ")
                print_anagrams(word, avl_tree)
            elif answer == '4':
                file = input("Please type the name of the file: ")
                highest_anagrams = most_anagrams(file, avl_tree)
                print("The word with the most anagrams is:", highest_anagrams)
            else:
                print("Your option is not valid.")

            loop = input("\nWould you like to perform a new operation? y/n\n")

            if loop == 'y':
                keep_going = True
            elif loop == 'n':
                keep_going = False
            else:
                print("You option is not valid, please try again.")

    elif tree == '2':
        file = input("Please type the name of your file: ")
        print("Please wait while the Red-Black Tree is generated.")
        start_time = time.time()
        rb_tree = create_rb_tree(file)
        end_time = time.time()
        print("--- %s seconds ---" % (end_time - start_time))
        keep_going = True
        while keep_going:
            print("Please choose an option to perform:")
            print("   1. Print Red-Black Tree.")
            print("   2. Get the number of anagrams from a word.")
            print("   3. Print all possible anagrams from a word.")
            print("   4. Get the word with the most possible anagrams in a file.")

            answer = input()

            if answer == '1':
                print_tree(rb_tree.root)
            elif answer == '2':
                word = input("Please type the word to search for anagrams: ")
                print(count_anagrams(word, rb_tree))
            elif answer == '3':
                word = input("Please type the word to search for anagrams: ")
                print_anagrams(word, rb_tree)
            elif answer == '4':
                file = input("Please type the name of the file: ")
                highest_anagrams = most_anagrams(file, rb_tree)
                print("The word with the most anagrams is:", highest_anagrams)
            else:
                print("Your option is not valid.")

            loop = input("\nWould you like to perform a new operation? y/n\n")

            if loop == 'y':
                keep_going = True
            elif loop == 'n':
                keep_going = False
            else:
                print("You option is not valid, please try again.")

    elif tree == '3':
        print("Thank you for using this program. Bye!")
    else:
        print("You typed an invalid option.")
        main()


main()
