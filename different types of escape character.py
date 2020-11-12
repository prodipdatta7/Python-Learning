
cat = "I'm a cat"
dog = 'I\'m a dog'
a_new_text = "I'm writing the text combined with single quotes ' and double quotes \""
print(a_new_text)
print(cat + dog)
#testing the activities of different escape characters
text = "\a Notice the ringing bell :D" # \a is used for ringing BEL
print(text)
# \b is used for ASCII backspace
text1 = "Original_Text \b Backspace"
print(text1)
# \f is used for form feed. form feed is a non-priontable character.
# it forces the printer to eject the current page and continue printing at the top of another
text2 = "formfeed = \f. This is another sentence."
print(text2)
# \v is used for vertical tab
text3 = "vertical tab = \v, Notice the effect"
print(text3)

