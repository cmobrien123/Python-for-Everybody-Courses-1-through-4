# ES = dict()
#
# # ES['one']= 'uno'
# ES={'one': 'uno', 'two': 'dos', 'three':'tres'}
# print(ES)
#
#
# try:
#     print(ES['four'])
# except:
#     print('not here')
#
#
# print(len(ES))
#
#
# ## this is how you test if something is in a dictionary
# x = list(ES.values())
# print('four' in x)
## something very powerful here is the speed to find if
##something is in a dict() does not change no matter the size

## exercise 1
# x = open('words.txt')
# # print(x)
# ES = dict()
# count = 0
# wordlist = list()
# for line in x:
#     line = line.rstrip()
#     words = line.split()
#     for i in words:
#         count = count +1
#         ES[i] = count
# print(ES)
# print('We' in ES)




# word = 'brontosaurus'
# d = dict()
# for tities in word:
#     if tities not in d:
#         d[tities]= 1
#     else:
#         d[tities] = d[tities]+1
# # print(d)
#
# for c in word:
#     d[c]= d.get(c,0)+1
# print(d)
# get is a more precise way, it looks at each key and then
## runs the


counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10 :
        print(key, counts[key])


#
# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# list = list(counts.keys())
# print(list)
# list.sort()
# print(list)
# for key in list:
#     print(key, counts[key])
### sorting and modifying a dict by the keys in that dict()


### example taking romeo and juliet file
# fname = 'romeo.txt'
# fhand= open(fname)
#
# counts =dict()
# for line in fhand:
#     line = line.rstrip()
#     line = line.translate(line.maketrans('', '', string.punctuation))
#     line = line.lower()
#     words= line.split()
#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] +=1
#
# print(counts)


# import string

# fname = input('Enter the file name: ')
# fname = 'romeo.txt'
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     exit()
#
# counts = dict()
# for line in fhand:
#     line = line.rstrip()
#     # line = line.translate(line.maketrans('', '', string.punctuation))
#     line = line.lower()
#     words = line.split()
#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] += 1
#
# print(counts)

####
## https://www.coursera.org/learn/python-data/lecture/rQKjf/9-1-dictionaries
# purse = dict()
# purse['money']= 12
# purse['candy']=65
#
# print(purse['money'])
# purse['money']=45
# print(purse['money'])


# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zquian', 'cwen']
# for name in names:
#     if name not in counts:
#         counts[name]= 1
#     else:
#         counts[name]+=1
#         #counts[name]= counts[name]+1
#         # (both of these do the same thing)
# print(counts)

# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zquian', 'cwen']
# for name in names:
#     counts[name] = counts.get(name,0)+1
#     ## the 0 is for a new name, the +1 is for an existing name
# print(counts)



# jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
# print(jjj.keys())
# print(list(jjj))
# ## both of these do the same thing
# ## in making a list of the keys from a dict
# print(jjj.items())
# ## makes a list of tuples
# for k,v in jjj.items():
#     print(k,v)








#
