class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, element):
        return self.__insertNode(element, self.root)

    def __insertNode(self, element, node):
        new_node = Node(element)
        if (self.root is None):
            self.root = new_node
            return

        while (node is not None):
            if (node.element > new_node.element):
                if (node.left is None):
                    node.left = new_node
                    return
                return self.insertNode(element, node.left)
            if (node.element < new_node.element):
                if (node.right is None):
                    node.right = new_node
                    return
                return self.insertNode(element, node.right)

    def search(self, element):
        return self.__searchNode(element, self.root)
    
    def __searchNode(self, element, root):
        if root is None:
            return
    
        if (root.element == element):
            return root.element
        if (element < root.element):
            return self.__searchNode(element, root.left)
        if (element > root.element):
            return self.__searchNode(element, root.right)
        
tree = BinarySearchTree()
tree.insert(11)
tree.insert(13)
tree.insert(10)
print(tree.search(11))
print(tree.search(20))

