####TUPLELS ARE IMMPUTABLE####

# t ='a', 'b', 'c'
# print(t)
# print(type(t))
## the () are recomended but not needed



## similar to lists and dictionaries, you can make an empyty one
# t = tuple()
# print(t)
# t = tuple('kitty cat')
# print(t)
## please don't make tuple a variable name



## indexing also works
# t = tuple('kitty cat')
# print(t[:5])
#
#
#
# ##but here is the kicker, you cannot modifiy
# t = tuple('kitty cat')
# t[1]='g'
# print(t)
# ## this gets a traceback


####COMPARING TUPELS####


# x = 0,1,2000000
# y = 0,3,4
# print(x<y)
## to compare size, it goes by the first value where there is a
## regardless of the others
## other function/methods are similar such as sort()



## sorting a word##


# txt = 'but soft what light in yonder window breaks'
# words = txt.split()
# t = list()
# for word in words:
#     t.append((len(word), word))
#     ## print(t)
#     ## you are creating a tuple within each list where
#     ## the fist value in the length and the second is
#     ## the word
# t.sort(reverse=True)
## print(t)
#     ## this says to go in revese order (from large to small)
# res = list()
# for length, word in t:
#     res.append(word)
# print(res)




####  TUPLE ASSIGNMENT ####


# m = ['have', 'fun']
# x,y = m
# print(x)
# print(y)



# a,b = b,a



# addr ='monty@python.org'
# uname, domain = addr.split('@')
# print(uname)
# print(domain)
#



####DICTIONARIES AND TUPELS#####



# d={'a':10,'b':1, 'c':45}
# t =list(d.items())
# print(t)
## makes a list of tuples from the dict()
## not sure why you need the list()



# d={'a':10,'b':1, 'c':45}
# t =list(d.items())
# t.sort()
# print(t)
## sort by the first variable (in this case a letter)



# d={'a':10,'b':1, 'c':45}
# for key, val in list(d.items()):
#     print(val, key)
##swap the keys and values



#
# d={'a':10,'b':1, 'c':45}
# l= list()
# for key,val in d.items():
#     l.append((val,key))
#     ##note the double brackets
# print(l)
# l.sort(reverse=True)
# print(l)
### sorting a tuble by value instead of key





## import romeo and Juliet text and sort by largest value
# import string
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0)+1

# Sort the dictionary by value
# lst = list()
# for key, val in list(counts.items()):
#     lst.append((val, key))
#

# lst.sort(reverse=True)
# for val, key in lst[:10]:
#     print(val, key)


## the second chunk of that can  be replaced
# print(sorted([(v,k) for k,v in counts.items()]))




#### TUBLES CAN BE THE KEY IN A DICT() ####


# first ='Colin'
# last = 'OBrien'
# number = 'number'
# d =dict()
# d[last, first]= '2034...'
# for last, first in d:
#     print(first,last, d[last,first])


#### Some review on what sequence does what ####
###list()###[]
##is mutable
###Tupel###()
##is immutable, like strings
## so things like sort, do not work (is changing it)
##reverse=True (high to low)
##reverse=False (low to high)


###Video###
###https://www.coursera.org/learn/python-data/lecture/0ou0N/10-tuples





#
