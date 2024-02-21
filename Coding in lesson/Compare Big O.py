# algorithm that has O(1)
def algorithm_1(arr1):
          t = 0
          time.sleep(t)
          x = arr1[0] + arr1[len(arr1)-1]
          return 
# ----------------------------

#algorithm has O(n)
def algorithm_2(arr2):
          n = len(arr2)
          total=0
          for i in range(n):
                    total +=arr2[i]
          return

                    
# ------------------------------

# algorithm with O(n2)
def algorithm_4(arr4): # this algorithm sorts a list of integers
          
          n = len(arr4)  
          for i in range(n-1): 
                    for j in range(0, n-i-1): 
                              if arr4[j] > arr4[j+1] : 
                                       arr4[j], arr4[j+1] = arr4[j+1], arr4[j]
          return 
# ------------------------------

def algorithm_3(arr3): # this algorithm sorts a list of integer but in different way
          
          for i in range(1, len(arr3)):
                    
                    key = arr3[i] 
                    j = i-1
                    
                    while j >=0 and key < arr3[j] :
                              arr3[j+1] = arr3[j] 
                              j -= 1
                    arr3[j+1] = key 
          return
#========================================

def genlist():  # generates a list of integer numbers of num number of elements 
          import random
          arr =[]
          num = int(input("Enter number of elements "))
          for i in range (0, num):
                    arr.append(random.randint(1, 30000))
          return arr  # arr is a list of random integers between 1 to 30000
# ====================================================

if __name__=="__main__":
          
        import timeit
        import time
        myarray1 = genlist() # generate a list of random numbers
        myarray2 = myarray1
          
######      Measuring the time it takes to sorth the list using first algorithm    ########
        starttime1 = timeit.default_timer()
        a = algorithm_1(myarray1) # call first algorthim 
        endtime1= timeit.default_timer()
        print("The time algorithm_1 took is : " , endtime1-starttime1, " Seconds")
   
## ######      Measuring the time it takes to sorth the list using second algorithm    ########
        starttime2 = timeit.default_timer()
        b = algorithm_2(myarray1) # call second algorthim
        endtime2 = timeit.default_timer()
        print("The time algorithm_2 took is : " , endtime2 - starttime2, " Seconds")
##         
########      Measuring the time it takes to sorth the list using first algorithm    ########
        starttime3 = timeit.default_timer()      
        c = algorithm_3(myarray1) # call third algorthim 
        endtime3 = timeit.default_timer()
        print("The time algorithm_3 took is : " , endtime3-starttime3, " Seconds")
##                   
##          # ---    Measuring the time it takes to sorth the list using first algorithm    ---------
        starttime4 = timeit.default_timer()
        d = algorithm_4(myarray2) # call 4th Algorithm sort algorithms 
        endtime4 =  timeit.default_timer()
        print("The time algorithm_4 took is : " , endtime4 - starttime4, " Seconds")
##       
##

