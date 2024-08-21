# import os module
# modules are other programs, or other bits of code, that we can pull into our program
# clear is for clearing the screen. It's the same as if we input "Clear" in the Git Bash

import os
os.system('clear')

#Print Hello World to the screen
print ("Hello World!")

'''
Triple single quotes also indicates comments
'''

#####################################
#
# Using Variables in Python - #5
#
#####################################

full_name = "Julian Chomicki"
print (full_name)

persona = full_name
print (persona)

#####################################
#
# Python Data Types - #6
#
#####################################

# Strings
# Numbers
# Lists
# Tuples
# Dictionaries
# Boolean

#Numbers
age = 31 #Numbers are never wrapped in quotation marks
print (age +1)

#Lists
names = ["Julian", "Candela"] # dentro de una lista podemos poner cualquier cosa
print (names[0]) # Prints Julian since Julian is the item in the position #0
print (names[1]) # Prints Candela since Candela is the item in the position #1

#Dictionaries
fav_pizza = {
	"Julian": "Pepperoni", #No te olvides de la coma!
	"Candela": "Mushroom"
}

print (fav_pizza["Julian"]) # Prints Pepperoni
print (fav_pizza["Candela"]) # Prints Mushroom

#Boolean
#prints either true or false

proof = True

print (proof) #Prints "True"

#####################################
#
# Python Version Control With Git and Github - #7
# https://www.youtube.com/watch?v=yYknmU_gBgs&list=PLCC34OHNcOtrZTjsC5qtn_X9eRAmGmGOI&index=7
#
#####################################


