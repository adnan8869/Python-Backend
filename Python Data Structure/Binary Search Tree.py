class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # Add data to the left subtree
            if self.left:   # If left child exists, recurse
                self.left.add_child(data)
            else:      # If no left child, create a new node
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements = []
        # Visit left subtree
        if self.left:
            elements += self.left.in_order_traversal()
        # Visit base node
        elements.append(self.data)
        # Visit right subtree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    
    def search(self, value):
        if self.data == value:
            return True

        if value < self.data:
            # Value might be in the left subtree
            if self.left:
                return self.left.search(value)
            else:
                return False

        if value > self.data:
            # Value might be in the right subtree
            if self.right:
                return self.right.search(value)
            else:
                return False
    
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root



if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    bst_root = build_tree(numbers)
    print("In-order Traversal:", bst_root.in_order_traversal())
    print("Search for 20:", bst_root.search(20))
    print("Search for 99:", bst_root.search(99)) 