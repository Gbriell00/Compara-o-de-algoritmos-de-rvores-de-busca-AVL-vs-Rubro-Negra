from structures.bst import Node, binarySearchTree


class AVLNode(Node):

    def __init__(self, value):
        super().__init__(value)
        self.height = 1

        
class AVLTree(binarySearchTree):

    def __init__(self):
        super().__init__()
        self.rotations = 0

    def _node_height(self, node):

        if node is None:
            return 0

        return node.height


    def _update_height(self, node):

        node.height = 1 + max(
            self._node_height(node.left),
            self._node_height(node.right)
        )

    
    def balance_factor(self, node):

        if node is None:
            return 0

        return (
            self._node_height(node.left)
            - self._node_height(node.right)
        )


    def _rotate_left(self, node):

        new_root = node.right
        temporary = new_root.left

        new_root.left = node
        node.right = temporary

        self._update_height(node)
        self._update_height(new_root)

        self.rotations += 1

        return new_root


    def _rotate_right(self, node):

        new_root = node.left
        temporary = new_root.right

        new_root.right = node
        node.left = temporary

        self._update_height(node)
        self._update_height(new_root)

        self.rotations += 1

        return new_root

    
    def _rotate_left_right(self, node):

        node.left = self._rotate_left(node.left)

        return self._rotate_right(node)

    
    def _rotate_right_left(self, node):

        node.right = self._rotate_right(node.right)

        return self._rotate_left(node)


    
    def _rebalance(self, node):

        # Update node height
        self._update_height(node)

        # Calculate balance factor
        bf = self.balance_factor(node)

        # Left-heavy subtree
        if bf > 1:

            if self.balance_factor(node.left) >= 0:
                return self._rotate_right(node)

            else:
                return self._rotate_left_right(node)

        # Right-heavy subtree
        if bf < -1:

            if self.balance_factor(node.right) <= 0:
                return self._rotate_left(node)

            else:
                return self._rotate_right_left(node)

        # Node is already balanced
        return node




    
    
    def _insert(self, node, value):

        # Base case: empty position
        if node is None:
            return AVLNode(value), True

        # Standard BST insertion
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

      
        return self._rebalance(node), inserted



    

    def _remove(self, node, value):

        # Base case
        if node is None:
            return None, False

        # Search for the value
        if value < node.value:
            node.left, removed = self._remove(
                node.left, value
            )

        elif value > node.value:
            node.right, removed = self._remove(
                node.right, value
            )

        else:
            # Node with zero or one child
            if node.left is None:
                return node.right, True

            if node.right is None:
                return node.left, True

            # Node with two children
            successor = self._min_node(node.right)
            node.value = successor.value

            node.right, _ = self._remove(
                node.right, successor.value
            )

            removed = True

        if not removed:
            return node, False
            
        return self._rebalance(node), True



    def is_valid_avl(self):

        if not self.is_valid_bst():
            return False

        valid, _ = self._validate_avl(self.root)

        return valid

    def _validate_avl(self, node):

        if node is None:
            return True, 0

        left_valid, left_height = self._validate_avl(
            node.left
        )

        right_valid, right_height = self._validate_avl(
            node.right
        )

        actual_height = 1 + max(
            left_height,
            right_height
        )

        bf = left_height - right_height

        valid = (
            left_valid
            and right_valid
            and abs(bf) <= 1
            and node.height == actual_height
        )

        return valid, actual_height



    def clear(self):

        self.root = None
        self.rotations = 0
