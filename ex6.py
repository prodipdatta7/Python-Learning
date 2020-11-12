# Strings and text

text = "There are %d types of people."%10
binary = 'binary'
donot = "don't"
text2 = "Those who know %s and those who %s"%(binary, donot)

hilarious = False
joke_evaluation  = "Isn't that joke so funny? %r" # quite interesting features
text_completion = joke_evaluation % hilarious # formatters value can be added later like this one
more_complex = "Here I added some specifier for the value %d %f %e %E but not the value immediately. This is another one which is a string %r"
completion_of_more_compelx_text = more_complex % (100, 0.544, 10e6, 10E5, "considering for the example only")
print(joke_evaluation % hilarious)
print(completion_of_more_compelx_text) # this is seriously some nice features of python indeed

# Note %r can be used in replace of any format specifier but it doesn't show the exact format of the value we want. It shows the raw data
# Better to use exact format specifier for different types of value