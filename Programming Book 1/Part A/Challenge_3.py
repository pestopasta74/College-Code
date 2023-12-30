numDays = int(input("Enter a number of days: "))

numHours = numDays * 24
numMins  = numHours * 60
numSecs = numMins * 60

print("In", str(numDays), "days there are:")
print(str(numHours) + " Hours")
print(str(numMins) + " Minutes")
print(str(numSecs) + " Seconds")
