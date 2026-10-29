
from structures.bst import Node, binarySearchTree

RED = True
BLACK = False


class RBNode(Node):

    def __init__(self, value):
        super().__init__(value)
        self.color = RED


class RedBlackTree(binarySearchTree):

    def __init__(self):
        super().__init__()
        self.rotations = 0
        self.color_flips = 0

    def _is_red(self, node):

        if node is None:
            return False

        return node.color == RED


    def _rotate_left(self, node):

        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        new_root.color = node.color
        node.color = RED

        self.rotations += 1

        return new_root

    def _rotate_right(self, node):

        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        new_root.color = node.color
        node.color = RED

        self.rotations += 1

        return new_root

    def _flip_colors(self, node):

        node.color = not node.color
        node.left.color = not node.left.color
        node.right.color = not node.right.color

        self.color_flips += 1

    def _fix_up(self, node):

        # Correct a red link leaning right
        if self._is_red(node.right) and not self._is_red(node.left):
            node = self._rotate_left(node)

        # Correct two consecutive red links on the left
        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._rotate_right(node)

        # Split a temporary node with two red children
        if self._is_red(node.left) and self._is_red(node.right):
            self._flip_colors(node)

        return node

    
    def insert(self, value):

        self.root, inserted = self._insert(
            self.root, value
        )

        if self.root is not None:
            self.root.color = BLACK

        return inserted

    
    def _insert(self, node, value):

        # Create a new red node
        if node is None:
            return RBNode(value), True

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

        # Restore LLRB properties
        if inserted:
            node = self._fix_up(node)

        return node, inserted


    def is_valid_rb(self):

        if not self.is_valid_bst():
            return False

        if self.root is None:
            return True

        if self.root.color != BLACK:
            return False

        valid, _ = self._validate_rb(self.root)

        return valid

    def _validate_rb(self, node):

        # External NIL nodes are black
        if node is None:
            return True, 1

        # Validate children recursively
        left_valid, left_black_height = self._validate_rb(
            node.left
        )

        right_valid, right_black_height = self._validate_rb(
            node.right
        )

        # A red node cannot have red children
        red_violation = (
            self._is_red(node)
            and (
                self._is_red(node.left)
                or self._is_red(node.right)
            )
        )

        # LLRB does not allow right-leaning red links
        right_red_violation = self._is_red(node.right)

        # Both paths must have the same black height
        same_black_height = (
            left_black_height == right_black_height
        )

        valid = (
            left_valid
            and right_valid
            and not red_violation
            and not right_red_violation
            and same_black_height
        )

        # Black nodes contribute one to black height
        black_height = left_black_height

        if node.color == BLACK:
            black_height += 1

        return valid, black_height

    def _move_red_left(self, node):

        self._flip_colors(node)

        if self._is_red(node.right.left):

            node.right = self._rotate_right(node.right)

            node = self._rotate_left(node)

            self._flip_colors(node)

        return node

    def _move_red_right(self, node):

        self._flip_colors(node)

        if self._is_red(node.left.left):

            node = self._rotate_right(node)

            self._flip_colors(node)

        return node

    def _delete_min(self, node):

        # The minimum node has no left child
        if node.left is None:
            return None

        # Prepare the left path for deletion
        if (
            not self._is_red(node.left)
            and not self._is_red(node.left.left)
        ):
            node = self._move_red_left(node)

        # Remove recursively
        node.left = self._delete_min(node.left)

        # Restore LLRB properties
        return self._fix_up(node)

    def _remove(self, node, value):

        if value < node.value:

            if (
                not self._is_red(node.left)
                and not self._is_red(node.left.left)
            ):
                node = self._move_red_left(node)

            node.left, _ = self._remove(node.left, value)

        else:

            if self._is_red(node.left):
                node = self._rotate_right(node)

            if value == node.value and node.right is None:
                return None, True

            if (
                not self._is_red(node.right)
                and not self._is_red(node.right.left)
            ):
                node = self._move_red_right(node)

            if value == node.value:

                successor = self._min_node(node.right)
                node.value = successor.value

                node.right = self._delete_min(node.right)

            else:
                node.right, _ = self._remove(node.right, value)

        return self._fix_up(node), True

    def remove(self, value):

        if self.root is None:
            return False

        if not self.search(value):
            return False

        if (
            not self._is_red(self.root.left)
            and not self._is_red(self.root.right)
        ):
            self.root.color = RED

        self.root, removed = self._remove(
            self.root, value
        )

        if self.root is not None:
            self.root.color = BLACK

        return removed

    def visualize(self):

        if self.root is None:
            print("Empty tree")
            return

        self._visualize_rb(self.root, 0)


    def _visualize_rb(self, node, level):

        if node is None:
            return

        self._visualize_rb(node.right, level + 1)

        color = "R" if self._is_red(node) else "B"

        print("    " * level + f"{node.value}({color})")

        self._visualize_rb(node.left, level + 1)



    def clear(self):

        self.root = None
        self.rotations = 0
        self.color_flips = 0
