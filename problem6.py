# Author: Emmalyn Holmquist
# Date: 8/29/2024

# Problem 6
# Write a function that takes time, temp, and ratio and calculates Maturity
# (based on a given formula)

import math #import math module

def maturity(time, temp, ratio): #define function
    print(23.7*time**3+(temp/273)+math.log(ratio))

time=10 #define parameters
temp=10
ratio=10

maturity(time, temp, ratio) #call statement
