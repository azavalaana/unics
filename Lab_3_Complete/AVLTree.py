class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, node):

        if self.root is None:
            self.root = node
            node.parent = None

        else:
            # binary search tree insert.
            current_node = self.root
            while current_node is not None:

                # Choose to go left or right
                if node.key < current_node.key:
                    # If left child is None, insert the new node
                    if current_node.left is None:
                        current_node.left = node
                        node.parent = current_node
                        current_node = None
                    else:
                        # Move left again
                        current_node = current_node.left
                else:
                    # If the right child is None, insert the new node
                    if current_node.right is None:
                        current_node.right = node
                        node.parent = current_node
                        current_node = None
                    else:
                        # Move right again
                        current_node = current_node.right

            # Rebalance from the new node's parent to the root.
            node = node.parent
            while node is not None:
                self.rebalance(node)
                node = node.parent

    def remove_node(self, node):

        if node is None:
            return False

        parent = node.parent

        # Root node with 1 child or none
        if node is self.root:
            if node.left is not None:
                self.root = node.left
            else:
                self.root = node.right

            if self.root is not None:
                self.root.parent = None

            return True

        # Internal node 2 children
        elif node.left is not None and node.right is not None:
            successor_node = node.right
            while successor_node.left is not None:
                successor_node = successor_node.left

            node.key = successor_node.key
            self.remove_node(successor_node)

            return True

        # Internal left child only else with right child
        elif node.left is not None:
            parent.replace_child(node, node.left)
        else:
            parent.replace_child(node, node.right)

        # node is gone. Anything that was below node that has persisted is already correctly
        # balanced, but ancestors of node may need rebalancing.
        node = parent
        while node is not None:
            self.rebalance(node)
            node = node.parent

        return True

    # Remove node with specific key
    def remove_key(self, key):
        node = self.search(key)
        if node is None:
            return False
        else:
            return self.remove_node(node)

    # Left rotation at the given node
    def rotate_left(self, node):
        right_left_child = node.right.left

        # 1. right child moves up to the node's position
        if node.parent is not None:
            node.parent.replace_child(node, node.right)
        else:  # node is root
            self.root = node.right
            self.root.parent = None

        # 2. node becomes the left child
        node.right.set_child('left', node)

        # 3. joins right_left_child as the right child of node
        node.set_child('right', right_left_child)

        return node.parent

    # Right rotation at the given node
    def rotate_right(self, node):
        left_right_child = node.left.right

        # 1. left child moves up to the node's position
        if node.parent is not None:
            node.parent.replace_child(node, node.left)
        else:  # node is root
            self.root = node.left
            self.root.parent = None

        # 2. node becomes the right child
        node.left.set_child('right', node)

        # 3. join left_right_child as the left child of node
        node.set_child('left', left_right_child)

        return node.parent

    # Updates the given node's height and rebalances the subtree
    def rebalance(self, node):

        node.update_height()

        # Check for imbalance
        if node.get_balance() == -2:

            # subtree is too big to the right.
            if node.right.get_balance() == 1:
                self.rotate_right(node.right)

            return self.rotate_left(node)

        elif node.get_balance() == 2:

            # subtree is too big to the left
            if node.left.get_balance() == -1:
                self.rotate_left(node.left)

            return self.rotate_right(node)

        # No imbalance
        return node

    # Search node with same key
    def search(self, key):
        current_node = self.root
        while current_node is not None:

            if current_node.key == key:
                return True
            elif current_node.key < key:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return False
