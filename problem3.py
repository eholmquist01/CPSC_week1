# Author: Emmalyn Holmquist
# Date: 8/29/2024

# Problem 3
# Write two functions that (1) calculates the area of a circle and
# (2) determines the area of a square. Then (3) create a function
# that computes the area between a circle nestled within a square.

import math #import math module

def area_circle(r): #function 1: area of a circle. used radius for parameters
    area=float(math.pi*r**2)
    return area

def area_square(l): #function 2: area of square, only need one edge because its a square
    area=float(l**2)
    return area

length=10 #set parameters
radius=2#

area_circle(length) #call functions 1 & 2
area_square(radius)

square_area=area_square(length) #set variable expressions for the return of functions 1, 2
circle_area=area_circle(radius)

def difference(s,c): #function 3: use info from functs. 1, 2 to find difference
    diff=float(s-c)
    print(diff)

difference(square_area, circle_area) #call difference function


