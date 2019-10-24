# RBTNode class
class RBTNode:
    def __init__(self, key, parent, is_red=False, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

        if is_red:
            self.color = "red"
        else:
            self.color = "black"

    # Returns true if both child nodes are black (None)
    def are_both_children_black(self):
        if self.left is not None and self.left.is_red():
            return False
        if self.right is not None and self.right.is_red():
            return False
        return True

    def count(self):
        count = 1
        if self.left is not None:
            count += self.left.count()
        if self.right is not None:
            count += self.right.count()
        return count

    def get_grandparent(self):
        if self.parent is None:
            return None
        return self.parent.parent

    def get_predecessor(self):
        node = self.left
        while node.right is not None:
            node = node.right
        return node

    def get_sibling(self):
        if self.parent is not None:
            if self is self.parent.left:
                return self.parent.right
            return self.parent.left
        return None

    def get_uncle(self):
        grandparent = self.get_grandparent()
        if grandparent is None:
            return None
        if grandparent.left is self.parent:
            return grandparent.right
        return grandparent.left

    def is_black(self):
        return self.color == "black"

    def is_red(self):
        return self.color == "red"

    def replace_child(self, current_child, new_child):
        if self.left is current_child:
            return self.set_child("left", new_child)
        elif self.right is current_child:
            return self.set_child("right", new_child)
        return False

    # Sets either the left or right child of this node
    def set_child(self, child_direction, child):
        if child_direction != "left" and child_direction != "right":
            return False

        if child_direction == "left":
            self.left = child
        else:
            self.right = child

        if child is not None:
            child.parent = self

        return True
