
days = "\nSat\nSun\n...\nFri"
print("Here are the days",days)
print("The days are %s"%days)
print("The days are %r"%days)

# It is notable here that the '\n' is not working when we use %r as a formatter.
#We knew before that %r is used for the purpose of raw data.So it shows everything as it is.

text = """By using something like three double quotes, we can write as many lines as we want.
Like, it is the 2nd line.
And this is the 3rd line.
We can go on like this as deep as we want.
"""
print(text)

#text = "this is just for testing that whether it work for only a single quote too.
#most probably not and you can try it out by removing the # form the beginning"
#print(text)
