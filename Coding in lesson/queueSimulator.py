queue = ["", "", "", "", "", ""]
tail = 0
head = 0

def isEmpty():
    global head, tail
    return head == tail


def isFull():
    global head, tail, queue
    return (tail + 1) % len(queue) == head



def pop():
    global head, tail, queue
    if not isEmpty():
        head += 1
        return queue[head - 1]
    else:
        print("Queue is empty")


def push(element):
    global head, tail, queue
    if not isFull():
        queue[tail] = element
        tail = tail + 1
        if tail == len(queue):
            tail = 0
    else:
        print("Queue is full")


def main():
    global head, tail, queue
    while True:
        print("1. Push")
        print("2. Pop")
        print("3. Exit")
        print("----------------------------------------")
        choice = input("Enter your choice: ")
        if choice == "1":
            element = input("Enter the element: ")
            push(element)
            print(f"queue is now {queue}")
            print("----------------------------------------")
        elif choice == "2":
            print(f"the value popped is {pop()}")
            print(f"queue is now {queue}")
            print("----------------------------------------")
        elif choice == "3":
            print("Thank you for using the queue simulator!")
            break
        else:
            print("Invalid choice, the choices are:")

main()
