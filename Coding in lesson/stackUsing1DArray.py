# declaring empty list, and initialising stackPointer.
names = ["", "", "", "", "", "", "", "", "", "", ""]
stackPointer = 0
maxLength = len(names)
# the above are global

running = True

def isEmpty():
    global stackPointer, maxLength, names
    if stackPointer == 0:
        return True
    else:
        return False


def isFull():
    global stackPointer, maxLength
    if stackPointer == maxLength:
        return True
    else:
        return False


def push(element):
    global stackPointer, maxLength, names
    if isFull():
        print("The stack is full")
    else:
        names[stackPointer] = element
        stackPointer += 1


def pop():
    global stackPointer, maxLength, names
    if isEmpty():
        print("Stack is empty")
    else:
        stackPointer -= 1


def main():
    choice = int(input("Do you want to push (enter 1), pop (enter 2), check if the stack is empty (enter 3), check if the stack is full (enter 4) or exit (enter 5) "))
    if choice == 1:
        data = input("Enter the name you want to push: ")
        push(data)
        print(names)
        print(stackPointer)
    elif choice == 2:
        name = pop()
        print(name)
        print(names)
        print(stackPointer)
    elif choice == 3:
        print(isEmpty())
    elif choice == 4:
        print(isFull())
    elif choice == 5:
        exit()
    else:
        print("You didn't enter a valid choice")

while running == True:
    main() # calling the main function