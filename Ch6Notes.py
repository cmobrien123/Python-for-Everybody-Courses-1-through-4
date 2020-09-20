# fruit = 'banana'
#
# # index = 5
# #
# # while index>=0:
# #     letter = fruit[index]
# #     print(letter)
# #     index = index -1
# # print('done')
#
# # print(fruit[:])
# #
# #
# #
# #
# # def count(Letter, word):
# #     count = 0
# #     for x in word:
# #         if x == Letter:
# #             count = count + 1
# #     print(count)
# #
# # count('a', fruit)
# # # print(test)
# # k=fruit.upper()
# # print(k,'!')
# line = 'Have a nice day'
# print(line.startswith('h'))
# print(line)









data ='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
a = data.find('@')
print(a)
s= data.find(' ',a) ## find the first ' ' after the @ (weridly they have the ' 'first)
print(s)
host = data[a+1:s]
print(host)






# camels = 42
# x= '%d' % camels
#
# print(x)
# print(type(x))
# print(type(camels))
#
# y= 'I have seen over %d camels' %camels
# print(y)
## you need the %camels at the end of this in order for it to work

#
# t = 'In %d years I have seen %g %s.' % (3,0.1,'camels')
# print(t)
### %d is integer
### %g is float
### %s is string



# st1 = 'hi'
# st2 = 'there'
# st3 = st1+" "+st2
# print(st3)
# pi = st1[1]
# # print(pi)
#

#
#
# # fruit = 'banana'
# #
# #
#
# index = 0
# while index < len(fruit):
#     x = fruit[index]
#     print(x)
#     index =  index+1
# print('done!')

#
#
# # for letter in fruit:
# #     print(letter)
# ## this is more elegant, aka shorter and easier to follow/less mistakes
#
# count= 0
# for x in fruit:
#     if x == 'a':
#         count= count+1
# print(count)

#
# s = 'Monty Python'
# '
# print(s[0:5])
# print(s[6:])
# print(s[6:10000])
# print(s[1:2])'
##note that the afer the : is up to but no including


# print(e)
#
## Z>a


# greet = 'Hello Bob'
# zap = greet.lower()
#
# print(zap)
#
# print('HI There'.lower())
#
# t= dir(zap)
# print(t)
## better to have a copy of the string library on you
# o =fruit.find('na')
# print(o)

# s = 'Monty Python     '
# # print(s)
# # x = s.lstrip()
# # print(x)
#
# x= s.startswith('M')
# print(x)
