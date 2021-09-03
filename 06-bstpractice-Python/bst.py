class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        if self.root is None:
            return Node(root)
        else:
            if self.root == new_val:
                return root
            elif self.root < new_val:
                self.right = insert(self.right, new_val)
            else:
                self.left = insert(self.left, new_val)
            return self
 

    def printSelf(self):
        # Your code goes here
        pass
        
    def search(self, find_val):
        # Your code goes here
        pass