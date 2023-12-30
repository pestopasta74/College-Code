square = [[0  ,1,   2,   3,   4,    5],
          [1, "A", "B", "C", "D", "E"],
          [2, "F", "G", "H", "I", "J"],
          [3, "K", "L", "M", "N", "O"],
          [4, "P", "Q", "R", "S", "T"],
          [5, "U", "V", "W", "X", "Y"],
          [6, "Z", "?", " ", "@", "."]]

# def display(square):



def deCipher(cryptogram):

    cryptogram = cryptogram.replace(" ", "")    # remove spaces
    crypto = cryptogram.split(",")              # split by comma and change converts to a list

    word = ""                                   # initialise the value of word to empty string

    #
    #
    #
    #
    return word

def main():
    print()

    code = input(" Enter Cryptogram (the ciphered message) ...  ")

    print("The Secret word is ... " + deCipher(code))

main()