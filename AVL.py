from main import BinarySearchTree
from main import Node

class AVL(BinarySearchTree):
    def __init__(self):
        self.root = None

    def insert(self, element):
        if self.root is None:
            self.root = Node(element)
        return self.__insertNode(element, self.root)
    
    def __insertNode(self, element, root):
        new_node = Node(element)
        if (root.element > element):
            if root.left is None:
                root.left = new_node
            self.__insertNode(element, root.left)
        if (root.element < element):
            if root.right is None:
                root.right = new_node
            self.__insertNode(element, root.right)
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)
        if balance > 1:
            if element < root.left.element:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
            
        if balance < -1:
            if element > root.right.element:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def get_height(self, root):
        if root is None:
            return 0
        return root.height

    def get_balance(self, root):
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def left_rotate(self, z):
        y = z.right
        t2 = y.left

        y.left = z
        z.right = t2 

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        t3 = y.right

        y.right = z
        z.left = t3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y
    
    def pre_order(self, root):
        if root is None:
            return
        print(f"#{root.element}(#{self.get_balance(root)})")
        self.pre_order(root.left)
        self.pre_order(root.right)

tree = AVL()
tree.insert(33)
tree.insert(13)
tree.insert(52)
tree.insert(9)
tree.insert(21)
tree.insert(61)
tree.insert(8)
tree.insert(11)
tree.pre_order(tree.root)
          
           

    


