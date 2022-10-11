print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
import datetime
now = datetime.datetime.now()
print("Current date and time: ")
print(str(now))
from math import pi
radius = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(radius) + " is: " + str(pi * radius**2))
import numpy
print(numpy.__version__)