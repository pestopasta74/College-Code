def lengthcheck(word, length, option):

# option 1: checking fixed length = l
    if option ==1:
        if len(word)== length:
            return True
        else:
            return False

# option 2 checking if the word has length not shorter than l
    elif option == 2:
        if len(word) >= length:
            return True

# option 3 checking if the word has length not longer than l
    elif option == 3:
        if len(word)<= length:
            return True
        else:
            return False
    else:
        print("the value of option can only takes values between 1 to 3")
        return


def rangeCheck(num, minimum, maximum):
# Checks weather a given number is in a certain range of numbers
    if minimum <= num <= maximum:
        return True
    else:
        return False


def checkDigit(number):
# Takes a number as a string and checks if it's valid using the Luhn algorithm
    split = list(number)

    # Convert the list of strings to list of integers
    for i in range(len(split)):  # 0, 1, 2, 3, ...
        split[i] = int(split[i])

    # Double every second digit
    for index, number in enumerate(split):
        if index % 2 == 1:
            continue
        number *= 2
        if number > 9:
            first_digit = number % 10
            second_digit = number // 10
            number = first_digit + second_digit
        split[index] = number


    total = sum(split)

    if total % 10 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    print(lengthcheck("Preston", 10, 3))
    print(rangeCheck(15, 1, 31))
    print(checkDigit("4137894711755904"))