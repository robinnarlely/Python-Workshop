# Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other

import math
import random

a1 = int(input("First Number - "))
a2 = int(input("Second Number - "))
a3 = int(input("Third Number - "))

def compare (a1,a2,a3):
    if (a1==a2):
        result = " not different values"
        return result
    elif (a2==a3):
        result = " not different values"
        return result
    elif (a3==a1):
        result = " not different values"
        return result
    else:
        result = "different values"
        return result
result = compare(a1,a2,a3)
print (result)



# Write a Python program that accept a positive number and subtract from this number the sum of its digits and so on. Continues this operation until the number is positive.

def positive(n):
    if(n>=0):
      print("The numbers are given below ")
      s = 0
      n_str = str(n)
      while (n > 0):
        n = n - sum([int(i) for i in list(n_str)])
        print (n)
        n_str = list(str(n))
        s = s + 1
      return s
    else:
        print("the entered number is not positive")
v1 = int(input("Enter a positive Number:" ))
count = positive(v1)
print("no of iteration used is ",count)



# Write a Python program to find the digits which are absent in a given mobile number

#Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once

# Write a Python program to find common divisors between two numbers in a given pair

