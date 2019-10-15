from RBNode import RBTNode


class RedBlackTree:
    def __init__(self):
        self.root = None

    def __len__(self):
        if self.root is None:
            return 0
        return self.root.count()

    def insert(self, key):
        new_node = RBTNode(key, None, True, None, None)
        self.insert_node(new_node)

    def insert_node(self, node):

        if self.root is None:
            self.root = node
        else:
            cur_node = self.root
            while cur_node is not None:
                if node.key < cur_node.key:
                    if cur_node.left is None:
                        cur_node.set_child("left", node)
                        break
                    else:
                        cur_node = cur_node.left
                else:
                    if cur_node.right is None:
                        cur_node.set_child("right", node)
                        break
                    else:
                        cur_node = cur_node.right

        node.color = "red"

        self.insertion_balance(node)

    def is_none_black(self, node):
        if node is None:
            return True
        return node.is_black()

    def is_not_empty_red(self, node):
        if node is None:
            return False
        return node.is_red()

    def rotate_left(self, node):
        right_left_child = node.right.left
        if node.parent is not None:
            node.parent.replace_child(node, node.right)
        else:  # node is root
            self.root = node.right
            self.root.parent = None
        node.right.set_child("left", node)
        node.set_child("right", right_left_child)

    def rotate_right(self, node):
        left_right_child = node.left.right
        if node.parent is not None:
            node.parent.replace_child(node, node.left)
        else:  # node is root
            self.root = node.left
            self.root.parent = None
        node.left.set_child("right", node)
        node.set_child("left", left_right_child)

    def insertion_balance(self, node):
        # If node is root, set color black
        if node.parent is None:
            node.color = "black"
            return

        if node.parent.is_black():
            return

        parent = node.parent
        grandparent = node.get_grandparent()
        uncle = node.get_uncle()

        # change parent and uncle from red to black to color grandparent red
        if uncle is not None and uncle.is_red():
            parent.color = "black"
            uncle.color = "black"
            grandparent.color = "red"
            self.insertion_balance(grandparent)
            return

        # If node is parent's right and parent is grandparent's left, rotate left at parent
        if node is parent.right and parent is grandparent.left:
            self.rotate_left(parent)
            node = parent
            parent = node.parent
        # If node is parent's left and parent is grandparent's right, rotate right at parent
        elif node is parent.left and parent is grandparent.right:
            self.rotate_right(parent)
            node = parent
            parent = node.parent

        # change parent black and grandparent red
        parent.color = "black"
        grandparent.color = "red"

        # If node is parent's left child, then rotate right at grandparent, otherwise rotate left at grandparent
        if node is parent.left:
            self.rotate_right(grandparent)
        else:
            self.rotate_left(grandparent)

    def _bst_remove(self, key):
        node = self.search(key)
        self._bst_remove_node(node)

    def _bst_remove_node(self, node):
        if node is None:
            return

        # Root node (with 1 or 0 children)
        elif node is self.root:
            if node.left is not None:
                self.root = node.left
            else:
                self.root = node.right

            if self.root is not None:
                self.root.parent = None

        # Internal, left child only else right child only
        elif node.left is not None:
            node.parent.replace_child(node, node.left)
        else:
            node.parent.replace_child(node, node.right)

        # Internal node with 2 child nodes
        if node.left is not None and node.right is not None:
            successor_node = node.right
            while successor_node.left is not None:
                successor_node = successor_node.left

            successor_key = successor_node.key

            self._bst_remove_node(successor_node)

            node.key = successor_key

    def remove(self, key):
        node = self.search(key)
        if node is not None:
            self.remove_node(node)
            return True
        return False

    def remove_node(self, node):
        if node.left is not None and node.right is not None:
            predecessor_node = node.get_predecessor()
            predecessor_key = predecessor_node.key
            self.remove_node(predecessor_node)
            node.key = predecessor_key
            return

        if node.is_black():
            self.prepare_for_removal(node)
        self._bst_remove(node.key)

        # One special case if the root was changed to red
        if self.root is not None and self.root.is_red():
            self.root.color = "black"

    def search(self, key):
        current_node = self.root
        while current_node is not None:
            # Return the node if the key matches.
            if current_node.key == key:
                return current_node
            # Move left if key is less than the node's key.
            elif key < current_node.key:
                current_node = current_node.left
            # Move right if key is bigger than the node's key.
            else:
                current_node = current_node.right

        # key not found
        return None
