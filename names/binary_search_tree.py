class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value is None:
            self.value = value
            return
        elif self.value > value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif self.value <= value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        root = self.value
        if root == target:
            return True

        if root >= target and self.left:
            return self.left.contains(target)
        elif root < target and self.right:
            return self.right.contains(target)
        else:
            return False