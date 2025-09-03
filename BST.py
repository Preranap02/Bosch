class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value == current_node.value:
            return  # no duplicates allowed
        elif value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)

    def inorder(self):
        return self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        result = []
        if node:
            result.extend(self._inorder_recursive(node.left))
            result.append(node.value)
            result.extend(self._inorder_recursive(node.right))
        return result

    def preorder(self):
        return self._preorder_recursive(self.root)

    def _preorder_recursive(self, node):
        result = []
        if node:
            result.append(node.value)
            result.extend(self._preorder_recursive(node.left))
            result.extend(self._preorder_recursive(node.right))
        return result

    def postorder(self):
        return self._postorder_recursive(self.root)

    def _postorder_recursive(self, node):
        result = []
        if node:
            result.extend(self._postorder_recursive(node.left))
            result.extend(self._postorder_recursive(node.right))
            result.append(node.value)
        return result

bst = BinarySearchTree()
elements = [10, 5, 15, 3, 7, 12, 18]
print("Elements in bst =", elements)
for el in elements:
 bst.insert(el)
print("Search 7:", bst.search(7))   # True
print("Search 6:", bst.search(6))   # False

print("Inorder traversal:", bst.inorder())     # [3, 5, 7, 10, 12, 15, 18]
print("Preorder traversal:", bst.preorder())   # [10, 5, 3, 7, 15, 12, 18]
print("Postorder traversal:", bst.postorder()) # [3, 7, 5, 12, 18, 15, 10]
