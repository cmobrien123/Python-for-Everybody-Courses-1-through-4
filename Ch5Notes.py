# n = 10
# while True:
#     print(n)
# #     n=n-1
# # print('done')
#
#
# while True:
#     line =  input('>')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#         print(line)
#
# print('Done!')
# friends = ['joe', 'glen', 'steve']
# for x in friends:
#     print('Happy New Year:', x)
#
# print('Done!')

#
# # total = 0
# # for x in [3,41,12,9,74,15]:
# #     total = total + x
# # print("count:", total)
# ## this is a common way to find the total amount of something (called an accumulator)
# ##FYI, the len() and sum() functions can do this
#
# # list = [3,41,12,9,74,15]
# # y = sum(list)
# # print(y)
#
# ## see pg 64
# largest = None
# print('Before', largest)
# for x in [3,41,12,9,74,15]:
#     if largest is None or x > largest:
#         largest = x
#         if x == 41:
#             break
#         ## break is used to get out of a loop (usually used for infinate loops, using an if statement)
#         ## escapes 1 loop, not all, moves to the next
#     print("Loop:", x, largest)
# print("largest:", largest)




# while True:
#     line = input('>')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('done!')

#
# largest_so_far = -1
# print('Before', largest_so_far)
# for largest_so_far in [3,41,12,9,74,15]:
#     if largest is None or largest_so_far > largest:
#         largest_so_far = largest
#     print("Loop:", largest_so_far, largest)
# print("After:", largest_so_far)

#
# test = "hi"
# print(type(test))

#
#
# largest_so_far = -1
# for i in [3,41,12,9,74,15]:
#     if largest_so_far == -1 or i < largest_so_far:
#         largest_so_far = i
#     print("Loop:", i, largest_so_far)
# print("After:", i, largest_so_far)
#
#
# zork = 0
# print("Before", zork)
# for thing in [9,41,12,3,74,15]:
#     zork = zork + thing
#     print(zork, thing)
# print('After', zork)


# print('Before')
# for value in [9,41,12,3,74,15]:
#     if value > 20:
#         print('Large number:', value)
# print('AFTER')



# found =  False
# print('Before', found)
# for value in [9,41,12,3,74,15]:
#     if value == 3:
#         found = True
#         print(value, found)
#     else:
#         found = False
#         print(value, found)
# print('Afer', found)

smallest_so_far = None
for i in [9,41,12,3,74,15]:
    if smallest_so_far is None:
        smallest_so_far = i
    elif i < smallest_so_far:
        smallest_so_far = i
    print("Loop:", i, smallest_so_far)
print("After:", i, smallest_so_far)

## is  and 'is not' are only for finding True, False and None
## 'is' is stronger than ==
