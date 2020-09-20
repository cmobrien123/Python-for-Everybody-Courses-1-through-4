fhand = open('mbox.txt')
# print(fhand)
# #
# inp = fhand.read()
# print(len(inp))
# print(inp[:20])

# count = 0
# for line in fhand:
#     line= line.rstrip()
#     if line.startswith('From:'):
#         count = count +1
#         print(line)
# print(count)

## the above takes everything starting with From: and removes the newline character that has been created

for line in fhand:
    line = line.strip()
    #skip uninteresting lines
    if not line.startswith('From:'):
        continue
    print(line)
## the above does the same as the other one but this is a way of thinking 'if not interesting (not From:), ignore'

# for line in fhand:
#     line= line.strip()
#     if line.find('@uct.ac.za') == -1: continue
#     print(line)
## if the line does NOT contain the @uct, continue and ignore

##################

# fname = input('Enter file name:')
# try:
#     fhand= open(fname)
# except:
#     print('that file name was not found, please try again')
#     exit()
# count = 0
# for line in fhand:
#     if line.startswith('From:'):
#         tcount = count + 1
# print(count)


####################

# fout = open('output.txt', 'w')
# print(fout)
# ##this creates a new file OR if the file name already existed, it overwrites it
# line1= 'this land is your land, \n'
# line2= 'this land is my land, \n'
# fout.close()
#
# fout = open('output.txt', 'r')
# for line in fout:
#     if line.startswith('this'):
#         print(line)


#
# xfile = open('mbox.txt')
# for cheese in xfile:
#     print(cheese)
#
# print('done!')



# fhand = open('mbox-short.txt')
# inp = fhand.read()
# print(len(inp))
# print(inp[:20])
