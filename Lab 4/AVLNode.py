# AVLNode class
class Node:

    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0

    # Assign either the left or right node with a new child
    def set_child(self, child_dir, child):

        if child_dir != "left" and child_dir != "right":
            return False

        # Assign the left or right node
        if child_dir == "left":
            self.left = child
        else:
            self.right = child

        if child is not None:
            child.parent = self

        self.update_height()
        return True

    # Replace a current child with a new child.
    def replace_child(self, cur_child, new_child):
        if self.left is cur_child:
            return self.set_child("left", new_child)
        elif self.right is cur_child:
            return self.set_child("right", new_child)
        return False

    # Calculate the current nodes' balance factor
    def get_balance(self):
        # Get height of left subtree
        left_height = -1
        if self.left is not None:
            left_height = self.left.height

        # Get height of right subtree
        right_height = -1
        if self.right is not None:
            right_height = self.right.height

        return left_height - right_height

    def update_height(self):
        # Get current height of left subtree
        left_height = -1
        if self.left is not None:
            left_height = self.left.height

        # Get current height of right subtree
        right_height = -1
        if self.right is not None:
            right_height = self.right.height

        # Assign new self.height with calculated height
        self.height = max(left_height, right_height) + 1
