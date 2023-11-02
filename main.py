class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
        self.parent = None


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
                    new_node.parent = node 
                    return
                return self.__insertNode(element, node.left)
            if (node.element < new_node.element):
                if (node.right is None):
                    node.right = new_node
                    new_node.parent = node
                    return
                return self.__insertNode(element, node.right)

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

    def count_children(self, node):
        num_children = 0
        if node.left != None: num_children+=1
        if node.right != None: num_children+=1
        return num_children
    
    # get the sucessor
    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def remove(self, element):
        return self.__removeNode(element, self.root)
    
    def __removeNode(self, element, node):
        if node is None:
            return  
        if (element < node.element):
            return self.__removeNode(element, node.left)
        if (element > node.element):
            return self.__removeNode(element, node.right)
        if (element == node.element):
            node_children = self.count_children(node)
            if node_children == 0:
                if node.parent.left == node:
                    node.parent.left = None
                    return
                else:
                    node.parent.right = None
                    return
            if node_children == 1:
                if node.left is not None:
                    child = node.left
                else:
                    child = node.right
                
                if node.parent.left == node:
                    node.parent.left = child
                else:
                    node.parent.right = child

                child.parent = node.parent
                return
            if node_children == 2:
                successor = self.min_value_node(node.right)
                node.element = successor.element
                node.right = self.__removeNode(successor.element, node.right)

                

                



tree = BinarySearchTree()
tree.insert(11)
tree.insert(13)
tree.insert(12)
tree.insert(14)
tree.insert(10)
print(tree.search(11))
print(tree.search(20))
print(tree.remove(13))
print()
