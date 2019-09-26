# Lab 2 Option A
# Antonio Zavala


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
            tack = track.next
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
    return


# Use a boolean array seen of length m+1 to indicate if elements in the array have been seen before.
# Then determine if there are duplicates by performing a single pass through the unsorted list.
def solution4(head):
    return


def main():
    # Creates a linked list from both record files
    head = two_files_one_list("activision.txt", "vivendi.txt")

    # Perform solution 1 and prints it
    print("- - - Solution 1 - - -")
    print_list(solution1(head))
    print("- - - End Test - - -")

    # Perform solution 2 and prints it
    print("- - - Solution 2 - - -")
    print_list(solution2(head))
    print("- - - End Test - - -")

    # Perform solution 3 and prints it
    print("- - - Solution 3 - - -")
    print_list(solution3(head))
    print("- - - End Test - - -")

    # Perform solution 4 and prints it
    print("- - - Solution 4 - - -")
    print_list(solution4(head))
    print("- - - End Test - - -")


main()

# remaining:
# add timers to methods
# add test lists to github
# solution 3 & 4
