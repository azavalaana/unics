# Lab 2 Option A
# Antonio Zavala
import time


# Node class
class Node(object):
    item = -1
    next = None

    # Constructor method for Node class
    def __init__(self, item, next):
        self.item = item
        self.next = next


# Method to create a linked list from a file
def file_to_list(file):
    txt = open(file)
    head = None

    for code in txt:
        head = Node(int(code), head)
    return head


# Method to create a linked list from two files
def two_files_one_list(file1, file2):
    txt1 = open(file1)
    txt2 = open(file2)
    head = None

    for code in txt1:
        head = Node(int(code), head)
    for code in txt2:
        head = Node(int(code), head)

    return head


# Method to print the linked list
def print_list(head):
    # In case of an empty list
    if head is None:
        print('the list is empty')

    # if the list contains at least one element
    else:
        current = head
        while current is not None:
            print(current.item)
            current = current.next


# Method that determine if there are duplicates by comparing each item with the item that follows it in the list.
def check_duplicates(head):
    duplicates = 0
    current = head
    to_compare = head.next

    while current.next is not None:
        if current.item == to_compare.item:
            duplicates += 1
            current = current.next
            to_compare = to_compare.next
        else:
            current = current.next
            to_compare = to_compare.next

    return duplicates


# Compare every element in the list with every other element in the list using nested loops
def solution1(head):
    if head is None:
        print('Empty List')
    elif head.next is None:
        print('One item in the list. Duplicates: 0')
    else:
        track = head  # keep track of current
        compare = head  # compare to current

        duplicate_head = None

        while track.next is not None:
            while compare is not None:
                if track == compare:
                    compare = compare.next
                if track.item == compare.item:  # used to found duplicates in the list
                    current = duplicate_head
                    inlist = False
                    while current is not None:  # check if node already on the duplicates
                        if current.item == track.item:
                            inlist = True
                        current = current.next
                    if not inlist:  # if it is not, add to duplicate list
                        duplicate_head = Node(track.item, duplicate_head)
                compare = compare.next
            compare = head
            track = track.next
        return duplicate_head


# Sort the list using bubble sort, then determine if there are duplicates
# by comparing each item with the item that follows it in the list
def solution2(head):
    if head is None:
        return head
    elif head.next is None:
        return head
    else:
        a = head
        current = head.next
        to_compare = head

        # temporal node for switching nodes in list
        temp = Node(-1, None)

        while a is not None:
            while current is not None:
                # If current is less than previous, switch nodes.
                if current.item < to_compare.item:
                    temp.item = to_compare.item
                    to_compare.item = current.item
                    current.item = temp.item
                current = current.next
                to_compare = to_compare.next
            to_compare = head
            current = head.next
            a = a.next
        return head


# Sort the list using merge sort (recursive), then determine if there are duplicates
# by comparing each item with the item that follows it in the list.
def solution3(head):
    # Base case
    if head is None:
        return None
    if head.next is None:
        return head
    else:
        # Find middle of list
        middle = middle_node(head)
        # Set the head of the second half
        second_half = middle.next
        # Break the first half
        middle.next = None

        # Recursive call to divide the lists again
        left = solution3(head)
        right = solution3(second_half)

        sorted_list = merge_and_sort_lists(left, right)
        return sorted_list


# Function that sorts and merges two lists (used for merge sort)
def merge_and_sort_lists(a, b):
    sorted_list = Node(-1, None)
    temp = sorted_list
    # Base case
    if a is None:
        sorted_list.next = b
    if b is None:
        sorted_list.next = a
    else:
        while a is not None or b is not None:
            if a is None:
                sorted_list.next = b
                b = b.next
            elif b is None:
                sorted_list.next = a
                a = a.next
            else:
                if a.item <= b.item:
                    sorted_list.next = a
                    a = a.next
                else:
                    sorted_list.next = b
                    b = b.next
            sorted_list = sorted_list.next
        sorted_list = temp.next  # Prevent -1 from being printed after the list has been sorted
    return sorted_list


# Method to get the middle node of the linked list
def middle_node(head):
    counter = head
    current = head
    count = 0
    middle = 0
    while counter.next is not None:
        count += 1
        counter = counter.next
    middle = count // 2
    counter = 0
    while counter != middle:
        current = current.next
        counter += 1
    return current


# Use a boolean array seen of length m+1 to indicate if elements in the array have been seen before.
# Then determine if there are duplicates by performing a single pass through the unsorted list.
def solution4(head):
    if head is None:
        return None
    else:
        # Find the largest ID to use as the size for the array
        largest_num = head.item
        current = head
        while current is not None:
            if current.item > largest_num:
                largest_num = current.item
            current = current.next

        seen = []
        for i in range(largest_num + 1):
            seen.append(False)

        dupl_list = None
        pointer = head

        while pointer is not None:
            # If seen for the first time, set the index at the same ID to True
            if seen[pointer.item] == False:
                seen[pointer.item] = True
            # Add duplicated IDs to the duplicates list if they have been seen
            else:
                pointer_duplicates = dupl_list
                prev_seen = False
                while pointer_duplicates is not None:
                    if pointer.item == pointer_duplicates.item:
                        prev_seen = True
                    pointer_duplicates = pointer_duplicates.next
                    # If haven't added yet, add it to the list
                if not prev_seen:
                    dupl_list = Node(pointer.item, dupl_list)
            pointer = pointer.next
    return dupl_list


def main():
    # Creates a linked list from both record files
    # CHANGE THE TEXT FILES NAMES TO THE VARYING TEXT FILES
    head = two_files_one_list("activision.txt", "vivendi.txt")

    # Perform solution 1 and prints it
    print("- - - Solution 1 - - -")
    start = time.time()
    print_list(solution1(head))
    end = time.time()
    print('Time elapsed:', (end - start))
    print("- - - End Test - - -")

    # Perform solution 2 and prints it
    print("- - - Solution 2 - - -")
    start = time.time()
    sol_2 = solution2(head)
    print_list(sol_2)
    print('Number of duplicates', check_duplicates(sol_2))
    end = time.time()
    print('Time elapsed:', (end - start))
    print("- - - End Test - - -")

    # Perform solution 3 and prints it
    print("- - - Solution 3 - - -")
    start = time.time()
    sol_3 = solution3(head)
    print_list(sol_3)
    print("Number of duplicates", check_duplicates(sol_3))
    end = time.time()
    print('Time elapsed:', (end - start))
    print("- - - End Test - - -")

    # Perform solution 4 and prints it
    print("- - - Solution 4 - - -")
    start = time.time()
    print_list(solution4(head))
    end = time.time()
    print('Time elapsed:', (end - start))
    print("- - - End Test - - -")


main()