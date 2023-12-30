#The School Lockers Puzzle - www.101computing.net/the-school-lockers-puzzle/

# Initialise a list of 1,000 values:
#   0 represents an open locker
#   1 represents a closed locker
# To start with, all lockers are open!

lockers = [0] * 1000

# Student 1 walks down the corridor and close all the lockers
student = 1
for p in range(0, 1000):
  for i in range(0, 1000, student):
    if lockers[i] == 1:
      lockers[i] = 0
    else:
      lockers[i] = 1
  student += 1
# At the end, the principal counts the number of closed lockers.
total = 0
for j in range(0,1000):
  total = total + lockers[j]

print(f"Total number of lockers closed: {total}")