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
            self.root = node
        elif self.root.value > new_val:
            if self.root.left is None:
                self.root.left = node
            else:
                return insert(self.root.left, node)
        else:
            if self.root.right is None:
                self.root.right = node
            else:
                return insert(self.root.right, node)


    def printSelf(self):
        # Your code goes here
        print(self.root)
        
    def search(self, find_val):
        # Your code goes here
        if self.root is None or self.root.value == find_val:
            return False
        return True
        if self.root.value < find_val:
            search(self.root.right, find_val)
        else:
            search(self.root.left, find_val)

