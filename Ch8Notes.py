numbers = [17, 123]
numbers[0] = 5
# x = 17 in numbers
# print(x)
print(numbers)
# # print(numbers)
#
#
# t = ['a,', 'b', 'c']
# # t.remove('b')
# # del t[1]
# # x= t.pop(1)
# # print(t)
# # print(t[1])
# # print(x)
#
# del t[0:2]
# print(t)

# total = 0
# count = 0
# while (True):
#     inp = input('Enter a number: ')
#     if inp == 'done':
#         print(count)
#         print(value)
#         print('Done!')
#         break
#     value = float(inp)
#     total = total + value
#     count = count + 1


# s= 'you a bitch'
# t = list(s)
# print(t)

s= 'you a bitch'
t = s.split()
print(t)
# print(t[2:3])
#
# s = 'spam-spam-spam'
# delimiter = '-'
# p=s.split(delimiter)
# print(p)
## used to make the breaks in a new list

# s= ['pining', 'for', 'the', 'fjords']
# delmeter= ' '
# y=delmeter.join(s)
# print(y)
## this is used to combine different elements of a list to make a stg
## notice the dif sntax from the breaking to make new list


# t1 = [1, 2]
# t2 = t1.append(3)
# print(t1)



#
# def chop(x):
#     t=x[1:-1]
#     print(t)
#     return None
#
#
# list= [1,2,3,4,5,6]
# chop(list)





# f = ['joe', 'steve', 'colin']
# for tities in f:
#     print('hi', tities)
# print(f[1])
#
# f[2]= 'corey'
# print(f)
# print(range(4))







# f = ['joe', 'steve', 'colin', 'tom', 'kellt', 'kelly']
#
# # for c in f:
# #     print('happy new year:', c)
#
# for i in range(4):
#     c=  f[i]
#     print(i,'happy new year:', c)






# f = ['joe', 'steve', 'colin', 'tom', 'kellt', 'kelly']
# x=f[3:4]
# print(x)


# c = list()
# c.append('book')
# c.append(99)
# print(c)

# f = ['joe', 'steve', 'colin', 'tom', 'kellt', 'kelly']
# print('joe' in f)
#
# f.sort()
# print(f)
# ## this puts it in alph. order



# numlist = list()
#
# while True:
#     inp = input('enter a number')
#     if inp == 'done':
#         break
#     value = float(inp)
#     numlist.append(value)
#
# average = sum(numlist)/len(numlist)
# print(average)



# abc = 'what you want'
# x = abc.split()
# for ti in x:
#     print(ti)
# #
# abc = 'what you             want '
# mod= abc.split()
# print(mod[2])
#
#
# dgf= 'bb;i;got it'
# g = dgf.split(';')
# print(g)
## the ; is caled a delimiter

#
fhand = open('mbox-short.txt')
for line in fhand:
    line =  line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])
#
# line= 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# words = line.split()




f ='Banana'
f[0] = 'b'
print(f)
## this will traceback because str, this only works for integer





# email = words[1]
# smaller = email.split('@')
# school = smaller[1]
# sname = school[:3]
# print(sname)
