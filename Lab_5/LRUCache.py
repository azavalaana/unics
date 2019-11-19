
class QNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return "(%s, %s)" % (self.key, self.value)


class LRUCache(object):
    def __init__(self, capacity):

        if capacity <= 0:
            raise ValueError("capacity > 0")
        self.hash_map = {}

        # No explicit doubly linked queue here (you may create one yourself)
        self.head = None
        self.end = None

        self.capacity = capacity
        self.current_size = 0

    # PUBLIC

    def get(self, key):

        if key not in self.hash_map:
            return -1

        node = self.hash_map[key]

        # small optimization (1): just return the value if we are already looking at head
        if self.head == node:
            return node.value
        self.remove(node)
        self.set_head(node)
        return node.value

    def set(self, key, value):

        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value

            # small optimization (2): update pointers only if this is not head; otherwise return
            if self.head != node:
                self.remove(node)
                self.set_head(node)
        else:
            new_node = QNode(key, value)
            if self.current_size == self.capacity:
                del self.hash_map[self.end.key]
                self.remove(self.end)
            self.set_head(new_node)
            self.hash_map[key] = new_node

    def max_capacity(self):
        return self.capacity

    def size(self):
        last = len(self.hash_map.keys())
        return last

    # PRIVATE

    def set_head(self, node):
        if not self.head:
            self.head = node
            self.end = node
        else:
            node.prev = self.head
            self.head.next = node
            self.head = node
        self.current_size += 1

    def remove(self, node):
        if not self.head:
            return

        # removing the node from somewhere in the middle; update pointers
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        # head = end = node
        if not node.next and not node.prev:
            self.head = None
            self.end = None

        # if the node we are removing is the one at the end, update the new end
        # also not completely necessary but set the new end's previous to be NULL
        if self.end == node:
            self.end = node.next
            self.end.prev = None
        self.current_size -= 1
        return node

    def print_elements(self):
        n = self.head
        print("[head = %s, end = %s]" % (self.head, self.end), end=" ")
        while n:
            print("%s -> " % (n), end="")
            n = n.prev
        print("NULL")


def main():
    lru = LRUCache(capacity=25)
    lru.set(6, 6)
    lru.set(5, 9)
    lru.set(8, 9)
    lru.set(9, 69)
    lru.set(15, 32)
    lru.print_elements()

    lru.get(5)
    lru.get(2)
    lru.print_elements()

    print("LRU Cache actual size:", lru.size())

    for i in range(lru.max_capacity()):
        lru.set(i, i * 3)
    lru.print_elements()
    lru.set(38, 9)
    lru.set(29, 69)
    lru.set(45, 32)
    lru.print_elements()

    print("max capacity: ", lru.max_capacity())
    print("LRU Cache actual size:", lru.size())


if __name__ == '__main__':
    main()
