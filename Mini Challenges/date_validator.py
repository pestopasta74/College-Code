# Dictionary to store the number of days in each month
month_days = {"01": 31, "02": 28, "03": 31, "04": 30, "05": 31, "06": 30, "07": 31, "08": 31, "09": 30, "10": 31, "11": 30, "12": 31}

# Boolean variable to control the main loop
running = True

# Checks if a given year is a leap year
def isLeap(year: int) -> bool:
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# Checks if the given date is in the format "dd/mm/yyyy"
def isValidDateFormat(date: str) -> bool:
    return len(date) == 10 and date[2] == '/' and date[5] == '/' and date[:2].isdigit() and date[3:5].isdigit() and date[6:].isdigit()

# Checks if a given day value is valid for the specified month and year
def isValidDay(day: int, month: str, year: int) -> bool:
    if isLeap(year):
        thisYear = month_days.copy()
        thisYear["02"] = 29
        return day <= month_days[month]
    else:
        return day <= month_days[month]

# Checks whether or not the string value of month is in the dictionary month_days
def isValidMonth(month: str) -> bool:
    return month in month_days

# Checks if the length of a year is correct
def isValidYear(year: int) -> bool:
    return len(str(year)) == 4

# Takes the user entered date value and checks if the date is valid
def valid(date: str) -> bool:
    if not isValidDateFormat(date):
        print("Invalid date format. Please enter the date in the format dd/mm/yyyy.")
        return False

    day = int(date[:2])
    month = date[3:5]
    year = int(date[6:10])
    return isValidYear(year) and isValidMonth(month) and isValidDay(day, month, year)

# Gets a value for the date that is getting validated and then prints whether or not the date is valid
def main() -> None:
    date: str = input("Please enter a date in the format dd/mm/yyyy: ")
    print(f"The date {date} is valid: {valid(date)}")

# Main loop to continue validating dates until the user decides to exit
while running:
    main()
    keepRunning: str = input("Do you want to continue validating dates? (y/n)")
    if keepRunning == "n":
        running = False
        print("Thank you for using the date validator!")
        exit()
