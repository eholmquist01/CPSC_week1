# Author: Emmalyn Holmquist
# Date: 8/29/2024

# Problem 2
# Write a function that takes two parameters for radius and the
#height of a cylinder and prints its volume.

import math #import math module

def findvol(r,h):
    areabase= float(math.pi*(r**2)) #find area of the base
    volume= float(areabase*h) #find volume based on base
    print(volume) #print volume

radius=10 #give parameters
height=30

findvol(radius, height) #call function