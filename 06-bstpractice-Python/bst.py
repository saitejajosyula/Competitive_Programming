class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Your code goes here
        node = Node(new_val)
        if self.root is None:
            self.root = Node
        elif root.value >= value:
            if root.left is None:
                root.left = Node
            else:
                insert(root.left, new_val)
        else:
            if root.right is None:
                root.right = Node
            else:
                insert(root.right, new_val)


    def printSelf(self):
        # Your code goes here
        pass
        
    def search(self, find_val):
        # Your code goes here
        if self.root is None or self.root.value == find_val:
            return root
        if root.value < find_val:
            return search(root.right, find_val)
        else:
            return search(root.left, find_val)

