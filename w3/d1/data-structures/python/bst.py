class Bst:
    def __init__(self):
        self.parent = None

    def insert(self, value):
        # This is where you will insert a value into the Binary Search Tree
        if self.parent is None:
            self.parent = Node(value)
            return

        current = self.parent

        while True:
            if value < current.data:
                if not current.left:
                    current.left = Node(value)
                    break
                current = current.left
            else:
                if not current.right:
                    current.right = Node(value)
                    break
                current = current.right

    def contains(self, value):
        # this is where you'll search the BST and return TRUE or FALSE if the value exists in the BST
        pass

    def remove(self, root, value):
        if not root:
            return root

        if root.data > value:
            root.left = self.remove(root.left, value)
        elif root.data < value:
            root.right = self.remove(root.right, value)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            temp_val = root.right
            mini_val = temp_val.data
            while temp_val.left:
                temp_val = temp_val.left
                mini_val = temp_val.data
            root.right = self.remove(root.right, root.data)
        return root


# ----- Node ------
class Node:
    # store your DATA and LEFT and RIGHT values here
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


bst = Bst()
bst.insert(10)
bst.insert(5)
bst.insert(20)
print(bst.parent.right)
print(bst.parent.left.data)
bst.remove(bst.parent, 5)
print(bst.parent.right.data)
