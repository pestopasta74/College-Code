def IsLeap(Year):
# Year is an integer
    Year = int(Year)
    if Year <=0:
        print("Years cannot have zero or negative values")
    if (Year % 100 ==0 and Year % 400 == 0) or (Year % 4 ==0):
        print("this is a leap year")
    else:
        print("this is not a Leap Year")

TestYear = input("Enter Year and I will check it if it is leap or not... ")
IsLeap(TestYear)