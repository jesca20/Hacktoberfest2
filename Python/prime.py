lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num) 


# using recursion : 

from math import sqrt
# prime function to check given number prime or not
def Prime(number, itr):  
    # base condition
    if itr == 1 or itr == 2:  
        return True
      # if given number divided by itr or not
    if number % itr == 0:  
        return False
      # Recursive function Call
    if Prime(number, itr - 1) == False:  
        return False

    return True

num = 13

itr = int(sqrt(num) + 1)

print(Prime(num, itr))



