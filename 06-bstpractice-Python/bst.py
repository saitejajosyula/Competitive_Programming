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
        if self.root == None:
            return newNode(new_val)
        
        if new_val < self.root.value:
            lchild = self.insert(self.root.left, new_val)
            root.left = lchild

        elif new_val > self.root.value:
            rchild = self.insert(self.root.right, new_val)
            root.right = rchild

        return self.root  


    def printSelf(self):
        # Your code goes here
        if self.left:
            self.left.printSelf()
        if self.right:
            self.right.printSelf()
        
    def search(self, find_val):
        # Your code goes here
        if self.root is None or self.root.value == find_val:
            return True
        return False
        if self.root.value < find_val:
            search(self.root.right, find_val)
        else:
            search(self.root.left, find_val)

