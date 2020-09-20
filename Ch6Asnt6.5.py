# Exercise  6.5: Take the following Python code that stores a string:
# string = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portion of the string after the
# colon character and then use the float function to convert the extraced string
# into a floating number.

text = "X-DSPAM-Confidence:    0.8475";


x=text.find(".")
y=text[x-1:x+5]
# print(y)
yint=float(y)
print(yint)
