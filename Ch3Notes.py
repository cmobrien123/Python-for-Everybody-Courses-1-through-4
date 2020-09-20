# x = 5.1
# if x== 5:
#     print('Yet')
# else:
#     int(x)
# if x== 5:
#     print('Yet')
# else:
#     print('No yet')
#     print(type(x))

#
# x=0
#
# if x<2:
#     print('small')
# elif x<10:
#     print('medium')
# else:
#     print('large')
#  ## you don't need the else, you can have the if/elif and if nothing it met, nothing executes
 ## also, remeber to have a space at the end of a block
 ## also, they go in order


astr = input('Enter a number:')
try:
    istr = int(astr) ## if this fails, we jump to except
    print('You did it!')
except:
    istr = -1
    print('No, Please enter a number. Not a word')


# try:
#     istr = int(astr) ## this works, so the except never happens
# except:
#     instr = -1
#
# print('Second', istr)
