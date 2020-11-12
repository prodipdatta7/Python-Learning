#Getting input from user

# **** Without using the Prompt ****

#There are two types of function to get input from the user in python
#input() and raw_input()
#raw_input() is only used in python 2.x
#the input get by the function input() is a string
#to convert it into the original format, we have to convert the type by following the rules of type conversion

print("How old are you?")
age = input() #got the age as a string
age = int(age) #converting the age into an int value. In case of raw_input(), we don't need it anymore
print("How tall are you?")
height = input() # in string format
print("How much do you weigh?")
weight = input() #in string format
print("So you are %r years old, %r tall and %r heavy"%(age, height, weight))

# *** Using The Prompt Here to get input ***

name = input("What's your name?\n") # used the prompt message inside the input function.
print("And your name is",name)
