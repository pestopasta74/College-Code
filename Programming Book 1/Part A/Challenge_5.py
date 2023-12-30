userInput = int(input("Enter a number: "))
match userInput:
    case 1:
        print("Thank you")
    case 2:
        print("Well done")
    case 3:
        print("Correct")
    case _:
        print("Error message")
