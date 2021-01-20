# Chapter 11 Notes: Regular Expressions
## need to import re before using reg. expressions



##### 11.1 #####



# Search for lines that contain 'From'
import re   ## dont forget this
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:',line):  ## like a find all function
        print(line)

# Search for lines that start with 'From'
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):  ## now a 'starts with'
        print(line)

# Search for lines that start with 'F', followed by
# 2 characters, followed by 'm:'
# using the period or '.'
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:', line):
        print(line)

# Search for lines that start with From and have an at sign
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@') #starts with From, has one or more characters after it (the period +) and contains @
        print(line)
## the + is one or more, * is 0 ore more

## the + and * are 'pushy' meaning that they will 'push' to the last character. ie if there are multiple @
## in a line, they will not stop until the they get to the last one (possible to turn off but complicated :-))



##### 11.2 #####



import re
t = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', t)   ## the \S+ has meaning in regular expressions
print(lst)
## \S+ matches to nonewhitespace characters
## note that since there is no non-white space before @2pm, its does not get picked up

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x= re.findall('\S+@\S+',line)
    if len(x)>0:  ## note that you need this so you don't just end up print every line
        print(x)


import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]',line)
    if len(x)>0:
        print(x)



##### 11.3 #####



import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S.*: [0-9.]+',line) ##note that inside the [] the period is just a period
    if len(x)>0:
        print(x)


import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)',line) ##using the () we are telling python that we just want that part
    if len(x)>0:
        print(x)

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):', line)
    if len(x) > 0:
        print(x)



##### 11.4 Escape Character #####

import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)


# Consolidated grouping of all regular expression characters:


# ˆ Matches the beginning of the line.
# $ Matches the end of the line.
# . Matches any character (a wildcard).
# \s Matches a whitespace character.
# \S Matches a non-whitespace character (opposite of \s).
# * Applies to the immediately preceding character(s) and indicates to match zero or more times.
# *? Applies to the immediately preceding character(s) and indicates to match zero or more times in “non-greedy mode”.
# + Applies to the immediately preceding character(s) and indicates to match one or more times.
# +? Applies to the immediately preceding character(s) and indicates to match one
# or more times in “non-greedy mode”.
# \b Matches the empty string, but only at the start or end of a word.
# \B Matches the empty string, but not at the start or end of a word.
# \d Matches any decimal digit; equivalent to the set [0-9].
# \D Matches any non-digit character; equivalent to the set [ˆ0-9].
# ? Applies to the immediately preceding character(s) and indicates to match zeroor one time.
# ?? Applies to the immediately preceding character(s) and indicates to match zeroor one time in “non-greedy mode”.
# [aeiou] Matches a single character as long as that character is in the specified set. In this example, it would match “a”, “e”, “i”, “o”, or “u”, but no other characters.
# [a-z0-9] You can specify ranges of characters using the minus sign. This example is a single character that must be a lowercase letter or a digit.
# [ˆA-Za-z] When the first character in the set notation is a caret, it inverts the logic. This example matches a single character that is anything other than an uppercase or lowercase letter.




### Square Brackets  ####


import re
x ='My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)
y = re.findall('[AEIOU]+',x)

#this is an example about being 'greedy' (or how not to be) using '?'
import re
x = 'From: Using the : character'
y = re.findall('^F.+?:',x)
print(y)



line = 'From Stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words=line.split()
email=words[1]
pieces = email.split('@')
print(pieces[1])


import re
line = 'From Stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y= re.findall('@([^ ]*)',line)
print(y)
print(type(y))

#
