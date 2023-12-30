"""
In this exercise we will use modulus 10 or mod 10 Luhn Algorithm to validate account number. The algorithm is also used to validate a credit card numbers, see the image of the right hand side.
Luhn algorithm Step by step
Consider the account number 79839693714
Split the account numbers to its digits.
Double the value of each second digit (even/odd digits).
If the doubling of the number (step 2) resulted in a two digits value, add the digits of the product.
Add the total of the numbers
If the total is multiple of 10, the account number is valid, see the examples.
"""

number = "4137894711755904"
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
    print("Omg it's valid")
else:
    print("Omg it's invalid")
