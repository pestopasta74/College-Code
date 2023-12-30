hundred = int(input("Enter a number over 100: "))
ten = int(input("Enter a number less than 10: "))
result = int

if hundred < 100:
    print("you did not enter a number over 100")
elif ten > 10:
    print("you did not enter a number less than 10")
else:
    result = hundred // ten
    remainder = hundred % ten
    print(f"{ten} goes into {hundred} {result} times with a remainder of {remainder}")


# Task the user to enter a number over 100 and then enter a number under 10 and
# tell them how many times the smaller number goes into the larger number in a user-friendly format.
