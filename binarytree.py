class NodeTree:
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key)


class BT:
    root = None

    def insert(self, root, node):
        if root is None:
            self.root = node
            return
        if node.key < root.key:
            if root.left is None:
                root.left = node
            else:
                self.insert(root.left, node)
        elif node.key > root.key:
            if root.right is None:
                root.right = node
            else:
                self.insert(root.right, node)

    def search(self, root, key):
        if root is None:
            return None
        if root.key == key:
            return root.value
        else:
            if key < root.key:
                return self.search(root.left, key)
            else:
                return self.search(root.right, key)

    def min(self, root):
        if root is None:
            return None
        if root.left is None:
            return root
        return self.min(root.left)

    def max(self, root):
        if root is None:
            return None
        if root.right is None:
            return root
        return self.max(root.right)

    def delete(self, root, key):
        if root is None:
            return None
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                return temp
            elif root.right is None:
                temp = root.left
                return temp

            temp = self.min(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root

    def print_in(self, root, level):
        if root is not None:
            self.print_in(root.left, level + 1)
            print("\t" * level, root)
            self.print_in(root.right, level + 1)

    def print_pre(self, root):
        if root is not None:
            print(root)
            self.print_pre(root.left)
            self.print_pre(root.right)

    def print_post(self, root):
        if root is not None:
            self.print_post(root.left)
            self.print_post(root.right)
            print(root)

    def getNodes(self, root):
        nodes = []
        self.collectNodes(root, nodes)
        return nodes

    def collectNodes(self, root, nodes):
        if root is not None:
            self.collectNodes(root.left, nodes)
            nodes.append(root.value)
            self.collectNodes(root.right, nodes)
