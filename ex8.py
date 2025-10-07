class LogEntry:
    def __init__(self, entry_time, visitor_name):
        self.entry_time = entry_time
        self.visitor_name = visitor_name

    def __repr__(self):
        return f"({self.entry_time}, {self.visitor_name})"


class Node:
    def __init__(self, data):
        self.data = data  
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _key(self, entry):
        return entry.visitor_name  

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)

        if self._key(data) < self._key(node.data):
            node.left = self._insert(node.left, data)
        elif self._key(data) > self._key(node.data):
            node.right = self._insert(node.right, data)
        else:
            node.data = data
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return None
        if key == self._key(node.data):
            return node.data
        elif key < self._key(node.data):
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < self._key(node.data):
            node.left = self._delete(node.left, key)
        elif key > self._key(node.data):
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            successor = self._min_value_node(node.right)
            node.data = successor.data
            node.right = self._delete(node.right, self._key(successor.data))
        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def traverse_in_order(self):
        result = []
        self._in_order(self.root, result)
        return result

    def _in_order(self, node, result):
        if node:
            self._in_order(node.left, result)
            result.append(node.data)
            self._in_order(node.right, result)

    def count(self):
        return self._count(self.root)

    def _count(self, node):
        if node is None:
            return 0
        return 1 + self._count(node.left) + self._count(node.right)

if __name__ == "__main__":
    bst = BinarySearchTree()
    
    bst.insert(LogEntry("10:00", "Alice"))
    bst.insert(LogEntry("09:30", "Bob"))
    bst.insert(LogEntry("10:15", "Charlie"))
    
    print("Search for Bob:", bst.search("Bob"))
    print("In-order traversal:", bst.traverse_in_order())
    print("Total entries:", bst.count())
    
    bst.delete("Bob")
    print("After deleting Bob:")
    print("In-order traversal:", bst.traverse_in_order())
    print("Total entries:", bst.count())
