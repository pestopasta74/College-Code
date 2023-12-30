#Bracket Validator - www.101computing.net/bracket-validator
from stack import Stack


def checkExpression(expression):
    stack = Stack()
    for character in expression:
        if character == "(":
            stack.push("(")
        elif character == ")":
            if stack.pop() == False:
                return False  # Invalid Expression
    if stack.isEmpty():
        return True  # Valid Expression
    else:
        return False  # Invalid expression


def checkExpression(expresssion):
    stack=Stack()
    for character in expression:
        if character=="(":
            stack.push("(")
        elif character==")":
            if stack.pop()==False:
                return False #Invalid Expression
        if stack.isEmpty():
            return True #Valid Expression
        else:
            return False #Invalid expression

#Main Program Starts Here
expression = input("Input an arithmetic expression: e.g. (5+2)*3:\n")
if checkExpression(expression):
    print("Bracket check: Valid expression.")
else:
    print("Bracket check: Invalid expression.")