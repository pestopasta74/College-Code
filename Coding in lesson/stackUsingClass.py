# Define a Stack class
class Stack:
    def __init__(self, max_size: int):
        """
        Initialize a Stack object.

        Args:
        - max_size: The maximum size of the stack.

        Returns:
        - None
        """
        self.stack = []  # Initialize an empty list to store the stack elements
        self.pointer = 0  # Initialize the pointer to 0
        self.max_size = max_size  # Set the maximum size of the stack

    def isEmpty(self) -> bool:
        """
        Check if the stack is empty.

        Returns:
        - True if the stack is empty, False otherwise.
        """
        return self.pointer == 0

    def isFull(self) -> bool:
        """
        Check if the stack is full.

        Returns:
        - True if the stack is full, False otherwise.
        """
        return self.pointer == self.max_size

    def push(self, element: any) -> None:
        """
        Push an element onto the stack.

        Args:
        - element: The element to be pushed onto the stack.

        Returns:
        - None
        """
        if self.isFull():
            print("Stack is full")
            return
        self.stack.append(element)  # Add the element to the stack
        self.pointer += 1  # Increment the pointer
        self.printStack()  # Print the current state of the stack

    def pop(self) -> any:
        """
        Pop an element from the stack.

        Returns:
        - The popped element if the stack is not empty, None otherwise.
        """
        if self.isEmpty():
            print("Stack is empty")
            return None
        element = self.stack.pop()  # Remove and return the last element from the stack
        self.pointer -= 1  # Decrement the pointer
        self.printStack()  # Print the current state of the stack
        return element

    def printStack(self) -> None:
        """
        Print the current state of the stack.

        Returns:
        - None
        """
        print("Stack:", self.stack)
        print("Pointer:", self.pointer)

def main() -> None:
    """
    The main function to run the stack program.

    Returns:
    - None
    """
    max_size = 5
    stack = Stack(max_size)  # Create a stack object with the specified maximum size
    actions = {
        '1': ('Enter the name you want to push: ', stack.push),
        '2': ('', stack.pop),
        '3': ('', stack.isEmpty),
        '4': ('', stack.isFull),
    }

    while True:
        choice = input("Do you want to push (enter 1), pop (enter 2), check if the stack is empty (enter 3), check if the stack is full (enter 4), or exit (enter any other key) ")
        action = actions.get(choice)

        if action:
            data = input(action[0]) if action[0] else None
            result = action[1](data) if data else action[1]()
            print(result if result is not None else '')
        else:
            break

main()
