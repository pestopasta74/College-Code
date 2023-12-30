class Stack():
    #Constructor
    def __init__(self, list=[]):
        # __ means private (our __stack attribute is private)
        self.__stack = []
        for value in list:
            self.__stack.append(value)

    def push(self, value):
        self.__stack.append(value)

    def pop(self):
        if len(self.__stack) > 0:
            return self.__stack.pop() #pop() Returns the value of the item that has been removed
        else: #Stack is empty
            return False

    def isEmpty(self):
        if len(self.__stack) == 0:
            return True
        else:
            return False
