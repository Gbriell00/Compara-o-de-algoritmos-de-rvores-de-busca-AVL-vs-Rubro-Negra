
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class binarySearchTree:


    
    
    def __init__(self):
        self.root = None


    
    
    def insert(self, value):
        self.root, inserted = self._insert(
            self.root, value
        )
        return inserted



    
    def _insert(self, node, value):

        if node is None:
            return Node(value), True

        if value < node.value:
            node.left, inserted = self._insert(
                node.left, value
            )

        elif value > node.value:
            node.right, inserted = self._insert(
                node.right, value
            )

        else:
            return node, False

        return node, inserted



    
    def search(self, value):
        current = self.root

        while current is not None:

                if value == current.value:
                    return True

                elif value < current.value:
                    current = current.left

                else:
                    current = current.right

        return False




    def in_order(self):
        result = []
        self._in_order(self.root, result)
        return result

    def _in_order(self, node, result):

        if node is None:
            return

        self._in_order(node.left, result)
        result.append(node.value)
        self._in_order(node.right, result)



    def height(self):
        return self._height(self.root)

    def _height(self, node):

        if node is None:
            return 0

        left_height = self._height(node.left)
        right_height = self._height(node.right)

        return 1 + max(
            left_height,
            right_height
        )

    
    def balance_factor(self, node):

        if node is None:
            return 0

        return (
            self._height(node.left)
            - self._height(node.right)
        )




    def visualize(self):

        if self.root is None:
            print("Empty tree")
            return

        self._visualize(self.root, 0)

    def _visualize(self, node, level):

        if node is None:
            return

        self._visualize(node.right, level + 1)

        print("    " * level + str(node.value))

        self._visualize(node.left, level + 1)



    def remove(self, value):
        self.root, removed = self._remove(
            self.root, value
        )
        return removed

    def _remove(self, node, value):

        if node is None:
            return None, False

        if value < node.value:
            node.left, removed = self._remove(
                node.left, value
            )

        elif value > node.value:
            node.right, removed = self._remove(
                node.right, value
            )

        else:
            # Case 1: no children
            if node.left is None and node.right is None:
                return None, True

            # Case 2: only right child
            if node.left is None:
                return node.right, True

            # Case 2: only left child
            if node.right is None:
                return node.left, True

            # Case 3: two children
            successor = self._min_node(node.right)
            node.value = successor.value

            node.right, _ = self._remove(
                node.right, successor.value
            )

            return node, True

        return node, removed

        
    def _min_node(self, node):

        current = node

        while current.left is not None:
            current = current.left

        return current



    def count_nodes(self):
        return self._count_nodes(self.root)

    def _count_nodes(self, node):
        if node is None:
            return 0

        return (
            1
            + self._count_nodes(node.left)
            + self._count_nodes(node.right)
        )




    def is_valid_bst(self):
        return self._is_valid_bst(
            self.root, None, None
        )

    def _is_valid_bst(self, node, minimum, maximum):

        if node is None:
            return True

        if minimum is not None and node.value <= minimum:
            return False

        if maximum is not None and node.value >= maximum:
            return False

        return (
            self._is_valid_bst(
                node.left, minimum, node.value
            )
            and
            self._is_valid_bst(
                node.right, node.value, maximum
            )
        )
