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
      print("The numbers are as below ")
      s = 0
      n_str = str(n)
      while (n > 0):
        n = n - sum([int(i) for i in list(n_str)])
        print (n)
        n_str = list(str(n))
        s = s + 1
      return s
    else:
        print("the number entered is not positive")
v1 = int(input("Input a positive Number:" ))
count = positive(v1)
print("number of iteration used is ",count)



# Write a Python program to find the digits which are absent in a given mobile number

a1 = []
a = int(input("Enter a mobile number (only 10 digit): "))
c = 0
while (c <= 9):
    a1.append(a % 10) 
    a = int ( a / 10 )
    c = c + 1

n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in a1:
    for j in n:
        if i == j:
            k=int(i)
            b[k] = True
l = 0
for m in b:
    if m == False:
       print(n[l],"is not present")
    l += 1



#Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once

import itertools  
var = "aeiou"
for i in itertools.permutations(var):
    print(i)



# Write a Python program to find common divisors between two numbers in a given pair

a =int(input("Input first number"))
b =int(input("Input second number"))
if a > b:
    g = a
    l = b
    if a % b == 0:
        print(b,"is a common divisor")
    i = 1
    while (i <= int(b/2)):
        if ((g % i == 0) and (l % i == 0)):
            print(i,"is a common divisor")
        i = i + 1
else:
    g = b
    l = a
    if b % a == 0:
        print(a,"is a common divisor")
    i = 1
    while (i <= int(a/2)):
        if ((g % i == 0) and (l % i == 0)):
            print(i,"is a common divisor")
        i = i + 1

