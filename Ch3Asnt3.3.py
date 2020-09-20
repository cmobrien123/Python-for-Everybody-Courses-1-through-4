# Exercise 3.Write a program to prompt for a score between 0.0 and 1.0. If the
# score is out of range, print an error message. If the score is between 0.0 and
# 1.0, print a grade using the following table:
# Score    Grade
# >= 0.9      A
# >= 0.8      B
# >= 0.7      C
# >= 0.6      D
# < 0.6      F
# ~~~
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F
# Run the program repeatedly as shown above to test the various, different
# values for input.

score = input("Give a score between 0.0 and 1.0")
s = float(score)
## note that g  is grade
try:
    if s>0 and s<=1:
        if s >=0.6 and s<0.7:
            G= "D"
        elif s>=0.7 and s<0.8:
            G= "C"
        elif s>=0.8 and s<0.9:
            G= "B"
        elif s>=0.9:
            G= "A"
        else:
            G="F"
    print(G)
except:
    print("Not able to calculate. Need number to be between 0.0 and 1.0")
