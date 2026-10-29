
from structures.avl import AVLTree
from structures.RB import RedBlackTree

def show_main_menu():

    print("\n" + "=" * 40)
    print("      AMAZON ENGINEERING CHALLENGE")
    print("=" * 40)

    print("1. AVL Tree")
    print("2. Red-Black Tree (LLRB)")
    print("3. Compare Trees")
    print("0. Exit")

    print("=" * 40)

def show_operations_menu(tree_name):

    print("\n" + "=" * 40)
    print(f"       {tree_name.upper()} OPERATIONS")
    print("=" * 40)

    print("1. Insert value")
    print("2. Remove value")
    print("3. Search value")
    print("4. In-order traversal")
    print("5. Visualize tree")
    print("6. Tree statistics")
    print("7. Validate tree")
    print("8. Clear tree")
    print("0. Back to main menu")

    print("=" * 40)


def read_integer():

    while True:

        user_input = input("Enter an integer value: ").strip()

        try:
            return int(user_input)

        except ValueError:
            print("Invalid input. Please enter an integer.")


def run_operations_menu(tree, tree_name):

    while True:

        show_operations_menu(tree_name)

        choice = input("Choose an option: ").strip()

        if choice == "1":

            value = read_integer()

            if tree.insert(value):
                print(f"Value {value} inserted successfully.")
            else:
                print(f"Value {value} already exists.")

        elif choice == "2":

            value = read_integer()

            if tree.remove(value):
                print(f"Value {value} removed successfully.")
            else:
                print(f"Value {value} was not found.")

        elif choice == "3":

            value = read_integer()

            if tree.search(value):
                print(f"Value {value} found.")
            else:
                print(f"Value {value} was not found.")

        elif choice == "4":

            print("In-order:", tree.in_order())

        elif choice == "5":

            print("\nTree structure:")
            tree.visualize()

        elif choice == "0":

            print("Returning to main menu...")
            break

       
        elif choice == "6":

            show_tree_statistics(tree, tree_name)

        elif choice == "7":

            validate_tree(tree)

        elif choice == "8":

            confirmation = input(
                "Clear the selected tree? (y/n): "
            ).strip().lower()

            if confirmation == "y":
                tree.clear()
                print("Tree cleared successfully.")

            else:
                print("Operation canceled.")

        else:

            print("Invalid option. Please try again.")


def show_tree_statistics(tree, tree_name):

    print("\n" + "=" * 40)
    print(f"{tree_name.upper()} STATISTICS")
    print("=" * 40)

    print("Number of nodes:", tree.count_nodes())
    print("Tree height:", tree.height())
    print("Total rotations:", tree.rotations)

    if isinstance(tree, RedBlackTree):
        print("Color flips:", tree.color_flips)

    print("=" * 40)



def validate_tree(tree):

    if isinstance(tree, AVLTree):
        valid = tree.is_valid_avl()

    elif isinstance(tree, RedBlackTree):
        valid = tree.is_valid_rb()

    else:
        print("Unknown tree type.")
        return

    if valid:
        print("Tree validation passed!")
    else:
        print("Tree validation failed!")







def main():

    avl_tree = AVLTree()
    rb_tree = RedBlackTree()

    while True:

        show_main_menu()

        choice = input("Choose an option: ").strip()

      
        if choice == "1":
            run_operations_menu(avl_tree, "AVL Tree")

        elif choice == "2":
            run_operations_menu(rb_tree, "Red-Black Tree")


        elif choice == "3":
            print("\nTree comparison is coming soon.")

        elif choice == "0":
            print("\nExiting program...")
            break

        else:
            print("\nInvalid option. Please try again.")










if __name__ == "__main__":
    main()
