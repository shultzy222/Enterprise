#!/usr/bin/ python3
# C# Code converted by Chris for DevOps class


from datetime import datetime
current_dateTime = datetime.now()

print ("Well Hello There")

# dd/mm/YY H:M:S
dt_string = current_dateTime.strftime("%d/%m/%Y %H:%M:%S")
print("The current date and time is " + dt_string)

#Type your name and press enter

name = input("Enter your name:")

#Create a string variable and get user input from the keyboard and store it in the variable and print

print ("Your username is: "+ name)

#Enter your age and convert from a string to an integer

age = input("Enter your age: ")
print ("your age is: "+ (age))
intAge = int(age)
